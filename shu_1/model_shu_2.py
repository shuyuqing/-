#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from chainer import Chain, cuda, Variable
import chainer.functions as F
import chainer.links as L
from chainer.links.connection.n_step_lstm import argsort_list_descent, permutate_list
import numpy as np
from sklearn.metrics import mean_squared_error

class LSTM(L.NStepLSTM):

    def __init__(self, in_size, out_size, dropout=0.0, use_cudnn=True):
        n_layers = 3
        super(LSTM, self).__init__(n_layers, in_size, out_size, dropout, use_cudnn)
        #原来cudnn是用来加速的
        self.state_size = out_size
        self.reset_state()

    def to_cpu(self):
        super(LSTM, self).to_cpu()
        if self.cx is not None:
            self.cx.to_cpu()
        if self.hx is not None:
            self.hx.to_cpu()

    def to_gpu(self, device=None):
        super(LSTM, self).to_gpu(device)
        if self.cx is not None:
            self.cx.to_gpu(device)
        if self.hx is not None:
            self.hx.to_gpu(device)

    def set_state(self, cx, hx):
        assert isinstance(cx, Variable)
        assert isinstance(hx, Variable)
        cx_ = cx
        hx_ = hx
        if self.xp == np:
            cx_.to_cpu()
            hx_.to_cpu()
        else:
            cx_.to_gpu()
            hx_.to_gpu()
        self.cx = cx_
        self.hx = hx_

    def reset_state(self):
        self.cx = self.hx = None

    def __call__(self, xs, train=True):
        batch = len(xs)
        if self.hx is None:
            xp = self.xp
            self.hx = Variable(
                    xp.zeros((self.n_layers, batch, self.state_size), dtype=xs[0].dtype))
        if self.cx is None:
            xp = self.xp
            self.cx = Variable(
                xp.zeros((self.n_layers, batch, self.state_size), dtype=xs[0].dtype))

        hy, cy, ys = super(LSTM, self).__call__(self.hx, self.cx, xs)
        self.hx, self.cx = hy, cy
        return ys

class SequentialBase(Chain):

    def __init__(self, **links):
        super(SequentialBase, self).__init__(**links)

    def _sequential_var(self, xs):
        if self._cpu:
            xs = [Variable(cuda.to_cpu(x)) for x in xs]
        else:
            xs = [Variable(cuda.to_gpu(x)) for x in xs]
        return xs

    def _accuracy(self, ys, ts):
        ys = permutate_list(ys, argsort_list_descent(ys), inv=False)
        ts = permutate_list(ts, argsort_list_descent(ts), inv=False)

        # print("打印预测值")
        # for g in ys:
        #     print(g.data)
        # print("打印标签")
        # for h in ts:
        #     print(h.data)

        correct = 0
        total = 0
        exact = 0
        for _y, _t in zip(ys, ts):
            y = _y.data
            t = _t.data
            _correct = (y == t).sum()
            _total = t.size
            if _correct == _total:
                exact += 1
            correct += _correct
            total += _total
        accuracy = correct / total
        self._eval = {'accuracy': accuracy, 'correct': correct, 'total': total, 'exact': exact}
        print("correct:%d"%correct)
        print("total:%d"%total)
        print("exact:%d"%exact)
        return accuracy

class BLSTMBase(SequentialBase):

    def __init__(self, f_dim, n_labels, dropout=0.0, train=True):
        #vocab_size, embed_size = embeddings.shape
        in_size = f_dim
        feature_size = 70 #embed_size#hidden_layer_size #100 is better
        #feature_size2 = 100
        super(BLSTMBase, self).__init__(
            embed = L.Linear(in_size, feature_size),
            f_lstm=LSTM(feature_size, feature_size, dropout),
            b_lstm=LSTM(feature_size, feature_size, dropout),
            linear=L.Linear(feature_size * 2, n_labels),
            # linear0=L.Linear(n_labels, n_labels),
        )
        self._dropout = dropout
        self._n_labels = n_labels
        self.train = train

    def reset_state(self):
        self.f_lstm.reset_state()
        self.b_lstm.reset_state()

    def __call__(self, xs):
        self.reset_state()
        xs_f = []
        xs_b = []
        hgg = 0
        for x in xs:
            hgg += 1
            x = x.astype(np.float32)#貌似要想用chainer的话就必需把它转化成np.float32这个类型
            # print("现在输出x")
            # print(x)
            _x = self.embed(self.xp.array(x))#关于xp,Array module for this link.Depending on which of CPU/GPU this link is on, this property returns:mod:`numpy` or :mod:`cupy`.
            # print("现在输出_x")
            # print(_x.data)
            # # os.system("pause")
            # print("现在输出_x后面的")
            # print(_x[::-1].data)
            # os.system("pause")

            xs_f.append(_x)
            xs_b.append(_x[::-1])#可以把整个特征值向量的排列顺序倒过来，进行逆向学习

        hs_f = self.f_lstm(xs_f, self.train)#把数据传入lstm
        # print("现在输出正向学习结果")
        # print(hs_f)
        hs_b = self.b_lstm(xs_b, self.train)#把数据逆向传入lstm
        # print("现在输出反向学习结果")
        # print(hs_b)
        # os.system("pause")
        ys = [self.linear(F.dropout(F.concat([h_f, h_b[::-1]]), ratio=self._dropout, train=self.train)) for h_f, h_b in zip(hs_f, hs_b)]


        y00=[]
        for y in ys:
            y0 = F.tanh(y)
            y00.append(y0)

        # print("现在输出最后结果")
        # for y in y00:
        #     print(y.data)
        # os.system("pause")
        return y00

class BLSTM(BLSTMBase):

    def __init__(self, f_dim, n_labels, dropout=0.0, train=True):
        super(BLSTM, self).__init__(f_dim, n_labels, dropout, train)

    def __call__(self, xs, ts):
        #当model这个实例被调用的时候就会执行这个函数
        loss = 0
        #print(type(ts))
        ts = self._sequential_var(ts)#labe
        ys = []
        hs= super(BLSTM, self).__call__(xs)#然后去执行它的父类的call,得到预测值
        #这部分可以把预测值输出来
        i = 1
        b = 0
        c = 0
        hs_1 = []
        ts_1 = []
        # print("第%d次前向传播的结果"%i)
        for m in hs:
            b = b + 1
            w = F.softmax(np.array(m.data,np.float32), axis=1)#注意啊，这个函数返回的是一个variable
            hs_1.append(w.data)
        # print(hs_1)
        i =i+1
        #这部分可以把预测值输出来

        for h,t in zip(hs_1,ts):#这部分是我的代码
            # h_1 = F.argmax(h, axis=1)#这个函数是预测的时候才需要的吧，训练的时候不需要
            h_1 = np.array(h,np.float32)
            t_1 = np.array(t.data,np.float32)
            # print("我是h_1")
            # print(h)
            # print("我是t")
            # print(t.data)
            # h_1 = np.array(h,np.float32)
            # t_1 = np.array(t.data,np.float32)
            loss += F.mean_squared_error(h_1,t_1)
            # print("我是loss")
            # print(loss.data)
            # ys.append(F.reshape(F.argmax(h, axis=1), t.shape))
        # for h, t in zip(hs, ts):#这部分代码是胡欢的
        #     print("问题在这里")
        #     print(h.data)
        #     print(t.data)
        #     loss += mean_squared_error(h.data, t.data)
        #     ys.append(F.reshape(F.argmax(h, axis=1), t.shape))
        # accuracy = self._accuracy(ys, ts)
        return loss

    def parse(self, xs, ts):#BLTSM
        print("---BLSTM PARCE----")
        #print(xs.shape)
        #hz.ys是预测值
        #ts是真实值
        ys = []
        ts = self._sequential_var(ts)  # labe
        hs = super(BLSTM, self).__call__(xs)
        # print("现在输出hs")
        # print(hs[0].data)
        # he = []
        # he = hs[0].data
        # return he
        # ys = []
        # for h in hs:
        # ys.append(cuda.to_cpu(h.data))
        # return ys
        for h,t in zip(hs,ts):
            ys.append(F.argmax(h, axis=1))

        # print("现在输出ys")
        # for i in ys:
        #     print(i.data)
        #
        # print("现在输出ts")
        # for w in ts:
        #     print(w.data)
        # print("现在输出ys")
        #
        # print(ys[0].data)
        # os.system("pause")
        accuracy = self._accuracy(ys, ts)
        return accuracy,ys[0].data#预测值



