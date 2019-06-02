import math,os
import numpy as np

def zhenggui(zhenggui_4,block):

    zhenggui_list_1 = []

    pingfanghe = 0

    # print(tezheng_1)
    N = block

    for d in zhenggui_4:
        # print(d)
        pingfanghe += math.pow(d, 2)

        # print(pingfanghe)
        # print(xishu)

    xishu = math.sqrt(N / pingfanghe)

    for u in zhenggui_4:

        zhenggui_list_1.append(u * xishu)

    zhenggui_list_1 = np.array(zhenggui_list_1)

    # print(zhenggui_list_1)

    return zhenggui_list_1


# zhenggui(zhenggui_4 = [1,2],block = 2)
