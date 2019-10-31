from __future__ import print_function
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

K.set_image_data_format('channels_first')
plot.switch_backend('agg')
sys.setrecursionlimit(10000)


def load_data(_feat_folder, _mono, _fold=None):
    feat_file_fold = os.path.join(_feat_folder, 'mbe_{}_fold{}.npz'.format('mon' if _mono else 'bin', _fold))
    dmp = np.load(feat_file_fold)
    _X_train, _Y_train, _X_test, _Y_test = dmp['arr_0'],  dmp['arr_1'],  dmp['arr_2'],  dmp['arr_3']
    return _X_train, _Y_train, _X_test, _Y_test


def get_model(data_in, data_out, _cnn_nb_filt, _cnn_pool_size, _rnn_nb, _fc_nb):

    spec_start = Input(shape=(data_in.shape[-3], data_in.shape[-2], data_in.shape[-1]))
    spec_x = spec_start
    for _i, _cnt in enumerate(_cnn_pool_size):
        spec_x = Conv2D(filters=_cnn_nb_filt, kernel_size=(3, 3), padding='same')(spec_x)
        spec_x = BatchNormalization(axis=1)(spec_x)
        spec_x = Activation('relu')(spec_x)
        spec_x = MaxPooling2D(pool_size=(1, _cnn_pool_size[_i]))(spec_x)
        spec_x = Dropout(dropout_rate)(spec_x)
    spec_x = Permute((2, 1, 3))(spec_x)
    spec_x = Reshape((data_in.shape[-2], -1))(spec_x)

    for _r in _rnn_nb:
        spec_x = Bidirectional(
            GRU(_r, activation='tanh', dropout=dropout_rate, recurrent_dropout=dropout_rate, return_sequences=True),
            merge_mode='mul')(spec_x)

    for _f in _fc_nb:
        spec_x = TimeDistributed(Dense(_f))(spec_x)
        spec_x = Dropout(dropout_rate)(spec_x)

    spec_x = TimeDistributed(Dense(data_out.shape[-1]))(spec_x)
    out = Activation('sigmoid', name='strong_out')(spec_x)

    _model = Model(inputs=spec_start, outputs=out)
    _model.compile(optimizer='Adam', loss='binary_crossentropy')
    _model.summary()
    return _model


def plot_functions(_nb_epoch, _tr_loss, _val_loss, _f1, _er, extension=''):
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


#######################################################################################
# MAIN SCRIPT STARTS HERE
#######################################################################################

is_mono = True  # True: mono-channel input, False: binaural input

feat_folder = r'C:\Users\a7825\Desktop\工作空间\语音数据\新建文件夹\npz'

__fig_name = '{}_{}'.format('mon' if is_mono else 'bin', time.strftime("%Y_%m_%d_%H_%M_%S"))


nb_ch = 1 if is_mono else 2
batch_size = 20    # Decrease this if you want to run on smaller GPU's
seq_len = 256       # Frame sequence length. Input to the CRNN.
nb_epoch = 500      # Training epochs
patience = int(0.25 * nb_epoch)  # Patience for early stopping

# Number of frames in 1 second, required to calculate F and ER for 1 sec segments.
# Make sure the nfft and sr are the same as in feature.py
sr = 44100
nfft = 2048
frames_1_sec = int(sr/(nfft/2.0))

print('\n\nUNIQUE ID: {}'.format(__fig_name))
print('TRAINING PARAMETERS: nb_ch: {}, seq_len: {}, batch_size: {}, nb_epoch: {}, frames_1_sec: {}'.format(
    nb_ch, seq_len, batch_size, nb_epoch, frames_1_sec))

# Folder for saving model and training curves
__models_dir = 'models/'
utils.create_folder(__models_dir)

# CRNN model definition
cnn_nb_filt = 128           # CNN filter size
cnn_pool_size = [5, 2, 2]   # Maxpooling across frequency. Length of cnn_pool_size =  number of CNN layers
rnn_nb = [32, 32]           # Number of RNN nodes.  Length of rnn_nb =  number of RNN layers
fc_nb = [32]                # Number of FC nodes.  Length of fc_nb =  number of FC layers
dropout_rate = 0.5          # Dropout after each layer
print('MODEL PARAMETERS:\n cnn_nb_filt: {}, cnn_pool_size: {}, rnn_nb: {}, fc_nb: {}, dropout_rate: {}'.format(
    cnn_nb_filt, cnn_pool_size, rnn_nb, fc_nb, dropout_rate))

avg_er = list()
avg_f1 = list()

for fold in [1,2,3,4]:

    print('\n\n----------------------------------------------')
    print('FOLD: {}'.format(fold))
    print('----------------------------------------------\n')

    # Load feature and labels, pre-process it
    X, Y, X_test, Y_test = load_data(feat_folder, is_mono, fold)
    # X是训练数据特征值，Y是训练数据的标签, X_test是测试数据特征值，Y_test是测试数据标签
    print('输出特征值')
    # print(X)
    print(X.shape)
    print('输出训练数据标签')
    # print(Y)
    print(Y.shape)
    # os.system('pause')


    X, Y, X_test, Y_test = preprocess_data(X, Y, X_test, Y_test, seq_len, nb_ch)
    print('学习数据')
    print(X.shape)
    # print(X)
    # print('训练数据')
    print('标签')
    print(Y.shape)
    # print(Y)
    os.system('pause')

    # Load model
    # os.system('pause')
    model = get_model(X, Y, cnn_nb_filt, cnn_pool_size, rnn_nb, fc_nb)#y的次元就直接决定了输出数据的次元
    # os.system('pause')

    # Training
    best_epoch, pat_cnt, best_er, f1_for_best_er, best_conf_mat = 0, 0, 99999, None, None
    tr_loss, val_loss, f1_overall_1sec_list, er_overall_1sec_list = [0] * nb_epoch, [0] * nb_epoch, [0] * nb_epoch, [0] * nb_epoch
    #[0]乘了500之后就变成[...]里面有500个零了
    posterior_thresh = 0.5
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

        os.system('pause')

        # Calculate the predictions on test data, in order to calculate ER and F scores
        pred = model.predict(X_test)

        # [[0.49399137 0.50213915 0.4922997  0.49658647 0.496524   0.49776226]
        #  [0.4942587  0.5022923  0.4924677  0.49617714 0.49634048 0.49762762]
        #  [0.4946595  0.50253636 0.49273133 0.4955582  0.49613088 0.4974213]
        # ...
        #  [0.49465695 0.50273037 0.49271172 0.49576327 0.49634126 0.49754673]
        #  [0.4942955  0.5024121  0.49243703 0.49627665 0.49652764 0.4977047]
        #  [0.49404386 0.5022036  0.49230117 0.49660677 0.49661395 0.4977997]]
        #  输出就是类似于这种一排一排的六个
        print(pred)
        print(pred.shape)
        # os.system('pause')


        pred_thresh = pred > posterior_thresh

        # print('pred_thresh')
        # print(pred_thresh)

        score_list = metrics.compute_scores(pred_thresh, Y_test, frames_in_1_sec=frames_1_sec)

        print('score_list[f1_overall_1sec]')
        print(score_list['f1_overall_1sec'])
        #0.5072815533980581
        print('score_list[er_overall_1sec]')
        print(score_list['er_overall_1sec'])
        #0.5072815533980581

        # os.system('pause')

        f1_overall_1sec_list[i] = score_list['f1_overall_1sec']
        er_overall_1sec_list[i] = score_list['er_overall_1sec']
        pat_cnt = pat_cnt + 1

        # Calculate confusion matrix
        test_pred_cnt = np.sum(pred_thresh, 2)
        Y_test_cnt = np.sum(Y_test, 2)
        conf_mat = confusion_matrix(Y_test_cnt.reshape(-1), test_pred_cnt.reshape(-1))
        conf_mat = conf_mat / (utils.eps + np.sum(conf_mat, 1)[:, None].astype('float'))

        if er_overall_1sec_list[i] < best_er:
            best_conf_mat = conf_mat
            best_er = er_overall_1sec_list[i]
            f1_for_best_er = f1_overall_1sec_list[i]
            model.save(os.path.join(__models_dir, '{}_fold_{}_model.h5'.format(__fig_name, fold)))
            best_epoch = i
            pat_cnt = 0

        print('tr Er : {}, val Er : {}, F1_overall : {}, ER_overall : {} Best ER : {}, best_epoch: {}'.format(
                tr_loss[i], val_loss[i], f1_overall_1sec_list[i], er_overall_1sec_list[i], best_er, best_epoch))
        plot_functions(nb_epoch, tr_loss, val_loss, f1_overall_1sec_list, er_overall_1sec_list, '_fold_{}'.format(fold))
        if pat_cnt > patience:
            break
    avg_er.append(best_er)
    avg_f1.append(f1_for_best_er)
    print('saved model for the best_epoch: {} with best_f1: {} f1_for_best_er: {}'.format(
        best_epoch, best_er, f1_for_best_er))
    print('best_conf_mat: {}'.format(best_conf_mat))
    print('best_conf_mat_diag: {}'.format(np.diag(best_conf_mat)))

print('\n\nMETRICS FOR ALL FOUR FOLDS: avg_er: {}, avg_f1: {}'.format(avg_er, avg_f1))
print('MODEL AVERAGE OVER FOUR FOLDS: avg_er: {}, avg_f1: {}'.format(np.mean(avg_er), np.mean(avg_f1)))
