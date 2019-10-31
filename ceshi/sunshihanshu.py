from __future__ import print_function
import os
import numpy as np
import time
import sys
import matplotlib.pyplot as plot
from sklearn.metrics import confusion_matrix
import metrics
import utils
from IPython import embed
import keras.backend as K
import label
from keras.losses import binary_crossentropy
from keras.activations import softmax

# x = [0.523,0.5645]
# x = np.array(x)
# shuzi = softmax(x)
# print(shuzi)
from sklearn.metrics import confusion_matrix


def hunxiao(juzhen):

    confuse = juzhen

    fause = confuse[1][1] / (confuse[1][0] + confuse[1][1])
    fause_1 = confuse[1][1] / (confuse[0][1] + confuse[1][1])
    correct = confuse[0][0] / (confuse[0][0] + confuse[0][1])
    correct_1 = confuse[0][0] / (confuse[0][0] + confuse[1][0])
    c = confuse[0][0] + confuse[0][1]
    f = confuse[1][0] + confuse[1][1]
    all = confuse[0][0] + confuse[0][1] + confuse[1][0] + confuse[1][1]
    fause_rate = f / all
    correct_rate = c / all
    correct_f = (2 * correct * correct_1) / (correct + correct_1)
    fause_f = (2 * fause * fause_1) / (fause + fause_1)

    return correct_f,fause_f,correct_rate,fause_rate

def hunxiao_1(juzhen):

    confuse = juzhen

    fause_f = (2*confuse[1][1])/(2*confuse[1][1] + confuse[0][1] + confuse[1][0])

    return fause_f


yucezhi   = [1,0,0,1,1,0,0,1,1,0,1,0,1]
yucezhi_1 = [1,1,0,1,0,1,0,1,0,1,0,1,0]

confuse = confusion_matrix(yucezhi, yucezhi_1)

correct_f,fause_f,correct_rate,fause_rate = hunxiao(confuse)
fause = hunxiao_1(confuse)

print(fause_f)
print(fause)

# yucezhi = np.random.rand(250, 2)
# yucezhi = np.argmax(yucezhi, axis=1)


# biaoqian = np.random.rand(250, 2)  # 生成标签
# r = [1, 0]
# for wi in range(250):
#     biaoqian[wi] = np.array(r)

# a = [[[0.5097386,0.49026144],[0.5097683,0.4902317 ]],[[0.5097342,0.49026585],[0.50975883,0.49024114]],[[0.50977415,0.49022588],[0.5097587,0.49024123]],[[0.50974196,0.49025804],[0.5097215,0.49027848]]]
# a = np.array(a)
# r = np.argmax(a, axis=1)

# print(yucezhi)
# print(biaoqian)
#
# biaoqian = label.label_2(biaoqian)
#
# print(biaoqian)
#
# confuse = confusion_matrix(biaoqian, yucezhi)
#
# print(confuse)


