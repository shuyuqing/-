import numpy as np
import os

def xuan(list):

    n = 0

    list_1 = list

    shanchu = []

    for i in list:

        if 0 not in i[1]:#把全是1的都删掉

            shanchu.append(n)

        if 1 not in i[1]:#把全是0的都删掉

            shanchu.append(n)

        n += 1

    # print('shanchu')
    # print(shanchu)

    list = np.delete(list,shanchu,0)

    # print(list)
    # print(list.shape)
    # os.system('pause')

    return list
