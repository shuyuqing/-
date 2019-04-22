#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def label_1(biaoqian):#用于模型mse

    biaoqian_1 = []
    biaoqian_2 = []
    # biaoqian_1=biaoqian.tolist()
    biaoqian_1 = biaoqian

    # print("标签的长度")
    # print(len(biaoqian_1))
    # print("标签的样子")
    # print(biaoqian_1)

    for i in range(len(biaoqian_1)):
        if biaoqian_1[i][0]==1:
            biaoqian_2.append([0,1])
        else:
            biaoqian_2.append([1,0])

    biaoqian_2 = np.array(biaoqian_2)
    # print(biaoqian_2)
    return biaoqian_2

def label_2(biaoqian):#用于模型cross

    biaoqian_1 = []
    biaoqian_2 = []

    biaoqian_1 = biaoqian

    for i in range(len(biaoqian_1)):
        if biaoqian_1[i][0]==1:
            biaoqian_2.extend([1])
        else:
            biaoqian_2.extend([0])

    biaoqian_2 = np.array(biaoqian_2)
    # print(biaoqian_2)
    return biaoqian_2

# if __name__ == "__main__":
#
#     i=np.array([[1],[0],[0],[0],[1]])
#     i = i.reshape((5,1))
#     print(i.shape)
#     label(i)
