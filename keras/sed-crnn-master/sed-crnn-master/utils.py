import os
import numpy as np

eps = np.finfo(np.float).eps


def create_folder(_fold_path):
    if not os.path.exists(_fold_path):
        os.makedirs(_fold_path)


def reshape_3Dto2D(A):
    return A.reshape(A.shape[0] * A.shape[1], A.shape[2])


def split_multi_channels(data, num_channels):
    in_shape = data.shape
    if len(in_shape) == 3:
        hop = in_shape[2] // num_channels
        tmp = np.zeros((in_shape[0], num_channels, in_shape[1], hop))
        for i in range(num_channels):
            tmp[:, i, :, :] = data[:, :, i * hop:(i + 1) * hop]

    elif len(in_shape) == 4:
        hop = in_shape[3] // num_channels
        tmp = np.zeros((in_shape[0], num_channels, in_shape[1], in_shape[2], hop))
        for i in range(num_channels):
            tmp[:, i, :, :, :] = data[:, :, :, i * hop:(i + 1) * hop]

    else:
        print("ERROR: The input should be a 3D matrix but it seems to have dimensions ", in_shape)
        exit()
    return tmp


def split_in_seqs(data, subdivs):

    # print(data.shape)
    # print('len of data')
    # print(len(data.shape))
    # os.system('pause')

    if len(data.shape) == 1:
        if data.shape[0] % subdivs:
            data = data[:-(data.shape[0] % subdivs), :]
        data = data.reshape((data.shape[0] // subdivs, subdivs, 1))

    elif len(data.shape) == 2:
        if data.shape[0] % subdivs:
            data = data[:-(data.shape[0] % subdivs), :]#取能够整除的那个部分，整除完多余的那部分数据掐掉
        data = data.reshape((data.shape[0] // subdivs, subdivs, data.shape[1]))#这样一来数据就被平均分成subdivs份了

    elif len(data.shape) == 3:
        if data.shape[0] % subdivs:
            data = data[:-(data.shape[0] % subdivs), :, :]
        data = data.reshape((data.shape[0] // subdivs, subdivs, data.shape[1], data.shape[2]))

    return data

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
