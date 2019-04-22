#!/usr/bin/env python
# -*- coding: utf-8 -*-
from chainer import Chain, cuda, Variable
import chainer.functions as F
import chainer.links as L
from chainer.links.connection.n_step_lstm import argsort_list_descent, permutate_list
import numpy as np
import config as cfg

class LSTM(L.NStepLSTM):

    def __init__(self, in_size, out_size, dropout=cfg.dropout, use_cudnn=cfg.cudnn):

    #  原来cudnn是用来加速的
        n_layers = cfg.lstmcenshu
        super(LSTM, self).__init__(n_layers, in_size, out_size, dropout, use_cudnn)

        # super(LSTM, self).__init__(n_layers, in_size, out_size, dropout, use_cudnn)
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
        return accuracy


class BLSTMBase(SequentialBase):

    def __init__(self, f_dim, n_labels, dropout=cfg.dropout, train=True):
        # vocab_size, embed_size = embeddings.shape
        in_size = f_dim
        feature_size = cfg.embed_size  # hidden_layer_size #100 is better
        # feature_size2 = 100
        super(BLSTMBase, self).__init__(
            embed=L.Linear(in_size, feature_size),
            f_lstm=LSTM(feature_size, feature_size, dropout),
            b_lstm=LSTM(feature_size, feature_size, dropout),
            linear=L.Linear(feature_size * 2, n_labels),
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
            x = x.astype(np.float32)  # 貌似要想用chainer的话就必需把它转化成np.float32这个类型

            _x = self.embed(self.xp.array(x))  # 关于xp,Array module for this link.Depending on which of CPU/GPU this link is on, this property returns:mod:`numpy` or :mod:`cupy`.
            xs_f.append(_x)
            xs_b.append(_x[::-1])  # 可以把整个特征值向量的排列顺序倒过来，进行逆向学习

        hs_f = self.f_lstm(xs_f, self.train)  # 把数据传入lstm
        hs_b = self.b_lstm(xs_b, self.train)  # 把数据逆向传入lstm
        # print(hs_f[0].data.shape)
        ys = [self.linear(F.dropout(F.concat([h_f, h_b[::-1]]), ratio=self._dropout, train=self.train)) for h_f, h_b in
              zip(hs_f, hs_b)]
        # print(ys[1].data.shape)
        # y00 = []
        # for y in ys:
        #     # y0 = self.linear0(y)
        #     # y00.append(y0)
        #     y0 = F.relu(y)
        #     y00.append(y0)
        # print(y00[0].data.shape)
        # print(y00[1].data.shape)
        # print(len(y00))
        # exit()
        # return y00
        return ys

class BLSTM(BLSTMBase):

    def __init__(self, f_dim, n_labels, dropout=cfg.dropout, train=True):
        super(BLSTM, self).__init__(f_dim, n_labels, dropout, train)

    def __call__(self, xs, ts):
        loss = 0
        # print(type(ts))
        ys = []
        ts = self._sequential_var(ts)  # labe
        hs = super(BLSTM, self).__call__(xs)
        for h, t in zip(hs, ts):
            # print("现在输出预测值")
            # print(h.data)
            # print("现在输出标签")
            # print(t.data)
            # os.system("pause")
            loss += F.softmax_cross_entropy(h,t)
            ys.append(F.argmax(F.softmax(h, axis=1), axis=1))
            # print("输出它们的loss")
            # print(loss.data)
            # os.system("pause")
        accuracy = self._accuracy(ys, ts)
        return loss,accuracy, ys

        # for m in hs:
        #     m = F.softmax(m, axis=1)  # 注意啊，这个函数返回的是一个variable
        # for h, t in zip(hs, ts):  # 这部分是我的代码
        #     loss += F.mean_squared_error(h, t)

    def parse(self, xs,ts):  # BLTSM

        print("---BLSTM PARCE----")
        loss = 0
        ys = []
        ts = self._sequential_var(ts)  # labe
        hs = super(BLSTM, self).__call__(xs)

        for h, t in zip(hs, ts):
            loss += F.softmax_cross_entropy(h, t)
            ys.append(F.argmax(F.softmax(h, axis=1), axis=1))

        accuracy = self._accuracy(ys, ts)
        return loss,accuracy, ys  # 预测值
        # 这是以前的版本
        # hs = super(BLSTM, self).__call__(xs)
        # he = []
        # he = hs[0].data
        # return he