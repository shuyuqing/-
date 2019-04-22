#!/usr/bin/env python
# -*- coding: utf-8 -*-

import chainer
import chainer.functions as F
import chainer.links as L
import numpy as np
from chainer import Chain, Variable
from chainer.backends import cuda
from chainer.links.connection.n_step_rnn import argsort_list_descent, permutate_list


class LSTM(L.NStepLSTM):
    def __init__(self, in_size, out_size, dropout=0, use_cudnn='auto'):
        n_layers = 2
        self.state_size = out_size
        with chainer.configuration.using_config('use_cudnn', use_cudnn):
            super(LSTM, self).__init__(n_layers, in_size, out_size, dropout)
        with self.init_scope():
            self.reset_state()

    def __call__(self, xs, train=True):
        batch = len(xs)
        if self.hx is None:
            xp = self.xp
            with chainer.using_config('volatile', 'auto'):
                self.hx = Variable(xp.zeros((self.n_layers, batch, self.state_size), dtype=xs[0].dtype))
        if self.cx is None:
            xp = self.xp
            with chainer.using_config('volatile', 'auto'):
                self.cx = Variable(xp.zeros((self.n_layers, batch, self.state_size), dtype=xs[0].dtype))

        with chainer.configuration.using_config('train', train):
            hy, cy, ys = super(LSTM, self).__call__(self.hx, self.cx, xs)
            self.hx, self.cx = hy, cy
            return ys

    def reset_state(self):
        self.hx = None
        self.cx = None

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


class SequentialBase(chainer.Chain):
    def __init__(self, **links):
        super(SequentialBase, self).__init__(**links)

    def _sequential_var(self, xs):
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
            _correct = (y == cuda.to_gpu(t)).sum()
            _total = t.size
            if _correct == _total:
                exact += 1
            correct += _correct
            total += _total
        accuracy = correct / total
        self._eval = {'accuracy': accuracy, 'correct': correct, 'total': total, 'exact': exact}
        return accuracy


class BLSTMBase(SequentialBase):
    def __init__(self, f_dim, n_labels, dropout=0, train=True):
        in_size = f_dim
        feature_size = 64  # embed_size#hidden_layer_size #100 is better
        super(BLSTMBase, self).__init__(
            embed=L.Linear(in_size, feature_size),
            f_lstm=LSTM(feature_size, feature_size, dropout, train),
            b_lstm=LSTM(feature_size, feature_size, dropout, train),

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
            x = x.data.astype(np.float32)

            _x = self.embed(self.xp.array(x))

            xs_f.append(_x)
            xs_b.append(_x[::-1])

        hs_f = self.f_lstm(xs_f, self.train)
        hs_b = self.b_lstm(xs_b, self.train)
        with chainer.using_config('train', self.train):
            ys = [
                self.linear(
                    F.dropout(
                        F.concat([h_f, h_b[::-1]]), ratio=self._dropout
                    )
                ) for h_f, h_b in zip(hs_f, hs_b)]
        return ys


class BLSTM(BLSTMBase):

    def __init__(self, f_dim, n_labels, dropout=0, train=True):
        super(BLSTM, self).__init__(f_dim, n_labels, dropout, train)

    def __call__(self, xs, ts):
        loss = 0
        ts = self._sequential_var(ts)  # label
        ys = []

        hs = super(BLSTM, self).__call__(xs)
        for h, t in zip(hs, ts):  # batch
            loss += F.softmax_cross_entropy(h.data, cuda.to_gpu(t.data))
            ys.append(F.reshape(F.argmax(h, axis=1), t.shape))

        accuracy = self._accuracy(ys, ts)
        return loss, accuracy

    def parse(self, xs):  # BLTSM
        print("---BLSTM PARSE----")
        hs = super(BLSTM, self).__call__(xs)
        label = 1
        ys = []
        for h in hs:
            ys.append(cuda.to_cpu(h.data))
        return ys
