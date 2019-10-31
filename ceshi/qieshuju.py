import numpy as np
import os

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
            data = data[:-(data.shape[0] % subdivs), :]#每次从数据的末尾往前抹，抹subdivs个数据
        data = data.reshape((data.shape[0] // subdivs, subdivs, data.shape[1]))

    elif len(data.shape) == 3:
        if data.shape[0] % subdivs:
            data = data[:-(data.shape[0] % subdivs), :, :]
        data = data.reshape((data.shape[0] // subdivs, subdivs, data.shape[1], data.shape[2]))

    return data


shuzu_1 = np.array([[1,2,3],[1,2,4],[2,3,2],[1,2,0],[4,5,2],[1,2,9],[2,1,9],[1,8,3]])



# print(shuzu_1[:-(shuzu_1.shape[0] % 3), :])
# print(shuzu_1[:-2])
# print(shuzu_1.shape)
# print(len(shuzu_1.shape))
# shuzu_1 = split_in_seqs(shuzu_1,3)
print(shuzu_1.reshape((shuzu_1.shape[0] //4, 4, shuzu_1.shape[1])))