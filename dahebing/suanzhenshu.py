import os
import numpy as np


def suanzhenshu(path):

    zuixiao = 999999
    zuida = 0
    zongzhenshu = 0

    path_1 = os.path.join(path,'data','fbank','all')
    geshu = len(os.listdir(path_1))

    for mulu in os.listdir(path_1):

        path_2 = os.path.join(path_1, mulu)

        f = open(path_2, 'r')

        a = np.loadtxt(f, delimiter=',', skiprows=0).astype(np.float32)

        zhenshu = len(a)

        zongzhenshu = zhenshu + zongzhenshu

        if zhenshu > zuida:

            zuida = zhenshu

        if zhenshu < zuixiao:

            zuixiao = zhenshu

        f.close()

    pinjun = zongzhenshu/geshu


    print('平均帧数是：%d'%pinjun)
    print("最大的是：%d"%zuida)
    print("最小的是：%d"%zuixiao)
