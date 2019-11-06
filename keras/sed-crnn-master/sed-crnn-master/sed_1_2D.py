# -*- coding: utf-8 -*-
from __future__ import print_function
from libs.base import App as AbstractApp, Logger as Log
import os
import numpy as np
import time
import sys
import matplotlib.pyplot as plot
from keras.layers import Bidirectional, TimeDistributed, Conv2D, MaxPooling2D, Input, GRU, Dense, Activation, Dropout, Reshape, Permute
from keras.layers.normalization import BatchNormalization
from keras.models import Model
from sklearn.metrics import confusion_matrix
import metrics
import utils
from IPython import embed
import keras.backend as K
import label
import config as cfg
from keras.optimizers import Adam #为了设置学习率
import tensorflow as tf
from keras.backend.tensorflow_backend import set_session
if cfg.gpuzhiding == True:
    config = tf.ConfigProto(gpu_options=tf.GPUOptions(visible_device_list=cfg.visible_device_list, allow_growth=True))
    set_session(tf.Session(config=config))

K.set_image_data_format('channels_first')
plot.switch_backend('agg')
sys.setrecursionlimit(10000)

def load_data(feat_folder_train,feat_folder_test):
    train = np.load(feat_folder_train)#把学习数据和训练数据都加载进来
    test = np.load(feat_folder_test)
    train = train['arr_0']
    test = test['arr_0']
    Xtrain = train[:, 1:None]
    Ytrain = train[:, 0:1]
    Ytrain = label.label_1(Ytrain)
    Xtest = test[:, 1:None]
    Ytest = test[:, 0:1]
    Ytest = label.label_1(Ytest)
    return Xtrain, Ytrain, Xtest, Ytest

def get_model(data_in, data_out, _cnn_nb_filt, _cnn_pool_size, _rnn_nb, _fc_nb):
    spec_start = Input(shape=(data_in.shape[-3], data_in.shape[-2], data_in.shape[-1]))
    spec_x = spec_start
    for _i, _cnt in enumerate(_cnn_pool_size):#给列表里面的元素加上序号
        spec_x = Conv2D(filters=_cnn_nb_filt, kernel_size=cfg.kernel_size, padding='same')(spec_x)
        spec_x = BatchNormalization(axis=1)(spec_x)
        spec_x = Activation('relu')(spec_x)
        spec_x = MaxPooling2D(pool_size=(1, _cnn_pool_size[_i]))(spec_x)
        spec_x = Dropout(dropout_rate)(spec_x)
    spec_x = Permute((2, 1, 3))(spec_x)
    spec_x = Reshape((data_in.shape[-2], -1))(spec_x)
    # for _r in _rnn_nb:
    #
    #     print(_r)
    #     # spec_x = Bidirectional(
    #     #     GRU(_r, activation='tanh', dropout=dropout_rate, recurrent_dropout=dropout_rate, return_sequences=True),
    #     #     merge_mode='mul')(spec_x)
    #
    #     spec_x = Bidirectional(GRU(units=_r, activation='tanh', recurrent_dropout=dropout_rate, return_sequences=False), batch_input_shape=(None, 8, 160), merge_mode='mul')(spec_x)

    spec_x = Bidirectional(GRU(units=_rnn_nb[0], activation='tanh', recurrent_dropout=dropout_rate, return_sequences=True),
                           # batch_input_shape=(None, 8, 160),
                           merge_mode='mul')(spec_x)
    spec_x = Bidirectional(GRU(units=_rnn_nb[1], activation='tanh', recurrent_dropout=dropout_rate, return_sequences=False),
                           # batch_input_shape=(None, 8, 32),
                           merge_mode='mul')(spec_x)
    # for _f in _fc_nb:
    #     spec_x = TimeDistributed(Dense(_f))(spec_x)
    #     spec_x = Dropout(dropout_rate)(spec_x)
    # spec_x = TimeDistributed(Dense(data_out.shape[-1]))(spec_x)
    # spec_x = TimeDistributed(Dense(data_out.shape[-1]))(spec_x)
    spec_x = Dense(_fc_nb)(spec_x)
    out = Activation('softmax', name='strong_out')(spec_x)
    _model = Model(inputs=spec_start, outputs=out)
    adam = Adam(lr = cfg.lr)
    _model.compile(optimizer=adam, loss='binary_crossentropy')
    _model.summary()
    return _model

def plot_functions(_nb_epoch, _tr_loss, _val_loss, _f1, _er, extension=''):#画图的函数
    plot.figure()
    plot.subplot(211)
    plot.plot(range(_nb_epoch), _tr_loss, label='train loss')
    plot.plot(range(_nb_epoch), _val_loss, label='val loss')
    plot.legend()
    plot.grid(True)
    plot.subplot(212)
    plot.plot(range(_nb_epoch), _f1, label='f')
    plot.plot(range(_nb_epoch), _er, label='er')
    plot.legend()
    plot.grid(True)
    plot.savefig(__models_dir + __fig_name + extension)
    plot.close()
    print('figure name : {}'.format(__fig_name))

def preprocess_data(_X, _Y, _X_test, _Y_test, _seq_len, _nb_ch):
    # 把数据_seq_len毎に切开
    # split into sequences
    _X = utils.split_in_seqs(_X, _seq_len)
    _Y = utils.split_in_seqs(_Y, _seq_len)
    _X_test = utils.split_in_seqs(_X_test, _seq_len)
    _Y_test = utils.split_in_seqs(_Y_test, _seq_len)
    _X = utils.split_multi_channels(_X, _nb_ch)
    _X_test = utils.split_multi_channels(_X_test, _nb_ch)
    return _X, _Y, _X_test, _Y_test

def preprocess_data_1(_X, _X_test, _seq_len, _nb_ch):
    # 把数据_seq_len毎に切开
    # split into sequences
    _X = utils.split_in_seqs(_X, _seq_len)
    _X_test = utils.split_in_seqs(_X_test, _seq_len)
    _X = utils.split_multi_channels(_X, _nb_ch)
    _X_test = utils.split_multi_channels(_X_test, _nb_ch)
    return _X, _X_test

#######################################################################################
#######################################################################################
is_mono = cfg.is_mono  # True: mono-channel input, False: binaural input
path_train = cfg.path_train  # 使用真实数据
path_test = cfg.path_test
__fig_name = '{}_{}'.format('mon' if is_mono else 'bin', time.strftime("%Y_%m_%d_%H_%M_%S"))
nb_ch = cfg.nb_ch
batch_size = cfg.batch_size            # Decrease this if you want to run on smaller GPU's
fft_point = cfg.fft_point
seq_len = cfg.seq_len       # Frame sequence length. Input to the CRNN.
nb_epoch = cfg.nb_epoch            # Training epochs
patience = cfg.patience  # Patience for early stopping
sr = cfg.sr
nfft = cfg.nfft
frames_1_sec = cfg.frames_1_sec
print('TRAINING PARAMETERS: nb_ch: {}, seq_len: {}, batch_size: {}, nb_epoch: {}, frames_1_sec: {}'.format(nb_ch, seq_len, batch_size, nb_epoch, frames_1_sec))
Log.i('TRAINING PARAMETERS: nb_ch: %d, seq_len: %s, batch_size: %d, nb_epoch: %d, frames_1_sec: %s' % (nb_ch,seq_len,batch_size,nb_epoch,frames_1_sec))
__models_dir = 'models/'
utils.create_folder(__models_dir)
cnn_nb_filt = cfg.cnn_nb_filt           # CNN filter size
cnn_pool_size = cfg.cnn_pool_size   # Maxpooling across frequency. Length of cnn_pool_size =  number of CNN layers
rnn_nb = cfg.rnn_nb           # Number of RNN nodes.  Length of rnn_nb =  number of RNN layers                        # rnn的层数等于rnn_nb的长度
fc_nb = cfg.fc_nb                # Number of FC nodes.  Length of fc_nb =  number of FC layers
dropout_rate = cfg.dropout_rate          # Dropout after each layer
############################################################################################
############################################################################################




print('MODEL PARAMETERS:\n cnn_nb_filt: {}, cnn_pool_size: {}, rnn_nb: {}, fc_nb: {}, dropout_rate: {}'.format(cnn_nb_filt, cnn_pool_size, rnn_nb, fc_nb, dropout_rate))
Log.i('MODEL PARAMETERS: cnn_nb_filt: %d, cnn_pool_size: %d,%d,%d, rnn_nb: %d,%d, fc_nb: %d, dropout_rate: %f'
      %(cnn_nb_filt,cnn_pool_size[0],cnn_pool_size[1],cnn_pool_size[2],rnn_nb[0],rnn_nb[1],fc_nb,dropout_rate))

avg_f1 = list()

for fold in [1]:
    print('\n\n----------------------------------------------')
    print('FOLD: {}'.format(fold))
    print('----------------------------------------------\n')

    # Load feature and labels, pre-process it
    # X, Y, X_test, Y_test = load_data(train_tezheng,test_tezheng)
    # X是训练数据特征值，Y是训练数据的标签, X_test是测试数据特征值，Y_test是测试数据标签
    # print('输出学习数据标签')
    # print(Y)
    # print(Y.shape)
    # os.system('pause')

    """生成虚拟数据
    a = np.random.rand(2000, 40)
    b = np.random.rand(250, 2)  # 生成标签
    r = [1, 0]
    for wi in range(250):
        b[wi] = np.array(r)
    aw = np.random.rand(2000, 40)
    bn = np.random.rand(250, 2)  # 生成标签
    r = [1, 0]
    for wi in range(250):
        bn[wi] = np.array(r)
    X = a
    Y = b
    X_test = aw
    Y_test = bn
    print('训练数据特征值')
    print(X.shape)
    print("训练数据标签")
    print(Y.shape)
    # os.system('pause')
    """
    train = np.load(path_train)
    test = np.load(path_test)

    X = train['arr_0']
    Y = train['arr_1']
    X_test = test['arr_0']
    Y_test = test['arr_1']

    Y = label.label_1(Y)#把标签转化为可以放入神经网络的样子
    Y_test = label.label_1(Y_test)#把标签转化为可以放入神经网络的样子

    print(X.shape)
    print(Y.shape)
    print('测试数据')
    print(X_test.shape)
    print(Y_test.shape)

    # os.system('pause')
    # X, Y, X_test, Y_test = preprocess_data(X, Y, X_test, Y_test, seq_len, nb_ch)#标签学习数据都切,用于每一帧都对应一个标签那种

    X, X_test = preprocess_data_1(X, X_test, seq_len, nb_ch)#只切割学习数据，用于一个block对应一个标签那种

    print('训练数据特征值')
    # print(X)
    print(X.shape)
    print("训练数据标签")
    # print(Y)
    print(Y.shape)
    # print('测试数据特征值')
    # print(X_test)
    # print(X_test.shape)
    # print('测试数据标签')
    # print(Y_test)
    # print(Y_test.shape)

    # Load model
    model = get_model(X, Y, cnn_nb_filt, cnn_pool_size, rnn_nb, fc_nb)

    # Training
    best_fscore, best_epoch, pat_cnt = 0, 0, 0
    tr_loss, val_loss, F_score, f1_overall_1sec_list, er_overall_1sec_list = [0] * nb_epoch, [0] * nb_epoch, [0] * nb_epoch, [0] * nb_epoch, [0] * nb_epoch

    for i in range(nb_epoch):
        print('Epoch : {} '.format(i), end='')
        hist = model.fit(
            X, Y,
            batch_size=batch_size,
            validation_data=[X_test, Y_test],
            epochs=1,
            verbose=1
        )
        val_loss[i] = hist.history.get('val_loss')[-1]
        tr_loss[i] = hist.history.get('loss')[-1]

        # Calculate the predictions on test data, in order to calculate ER and F scores
        pred = model.predict(X_test)
        pred = np.argmax(pred, axis=1)
        biaoqian = label.label_2(Y_test)
        confuse = confusion_matrix(biaoqian, pred)#计算混淆矩阵
        # correct_f, fause_f, correct_rate, fause_rate = utils.hunxiao(confuse)#计算f值以及两个种类的比率
        fause_f = utils.hunxiao_1(confuse)#计算f值以及两个种类的比率

        # print('fause_f')
        # print(fause_f)
        # os.system('pause')

        F_score[i] = fause_f
        pat_cnt = pat_cnt + 1

        if F_score[i] > best_fscore:

            best_fscore = F_score[i]
            model.save(os.path.join(__models_dir, '{}_fold_{}_model.h5'.format(__fig_name, fold)))
            # Log.i('save model:%s'%os.path.join(__models_dir, '{}_fold_{}_model.h5'.format(__fig_name, fold)))
            best_epoch = i
            pat_cnt = 0

        print('tr Er : {}, val Er : {}, F1 : {}, best_epoch: {}'.format(tr_loss[i], val_loss[i], F_score[i], best_epoch))
        Log.i('tr Er : %f, F1 : %f, epoch : %d, val Er : %f,  best_epoch : %d, LR : %f'%(tr_loss[i], F_score[i], i+1,val_loss[i], best_epoch, cfg.lr))
        plot_functions(nb_epoch, tr_loss, val_loss, f1_overall_1sec_list, er_overall_1sec_list, '_fold_{}'.format(fold))#画图的函数
        if pat_cnt > patience:
            break

    avg_f1.append(best_fscore)
    print('saved model for the best_epoch: {} with best_f1: {}'.format(
        best_epoch, best_fscore))
    Log.i("saved model for the best_epoch: %d with best_f1: %s"%(best_epoch,best_fscore))
    # print('best_conf_mat: {}'.format(best_conf_mat))
    # print('best_conf_mat_diag: {}'.format(np.diag(best_conf_mat)))

print('\n\nMETRICS FOR ALL FOUR FOLDS: avg_f1: {}'.format(avg_f1))
print('MODEL AVERAGE OVER FOUR FOLDS: avg_f1: {}'.format( np.mean(avg_f1)))
