import os
import numpy as np


def shujuzhengli(path,guanjianzi,dataname):

    X_train = None

    for file in os.listdir(path):

        path_1 = os.path.join(path,file,guanjianzi)

        for wenjian in os.listdir(path_1):

            wenjian = os.path.join(path_1,wenjian)

            f = open(wenjian, 'r')

            tezhenzhi = np.loadtxt(f, delimiter=',', skiprows=0).astype(np.float32)

            f.close()

            # tezhenzhi = np.loadtxt(wenjian)

            if X_train is None:
                X_train = tezhenzhi
            else:
                X_train = np.concatenate((X_train, tezhenzhi), 0)#把数据拼接成一个大的矩阵

    tmp_feat_file = os.path.join(path, dataname + '_.npz')

    np.savez(tmp_feat_file, X_train)#把每个wav文件的特征值保存为npz格式


shujuzhengli(path = r'C:\Users\a7825\Desktop\工作空间\桌面1\shiyan\cnn_3d',
           guanjianzi = 'mizhichuli_biaoqian_pingheng',
           dataname = 'er')

# a = np.load(r'C:\Users\a7825\Desktop\工作空间\桌面1\shiyan\symbol_40_8_8_biaoqian_pingheng/er_.npz')
# _X_train = a['arr_0']
# print(_X_train.shape)
# print(_X_train[112])
#
