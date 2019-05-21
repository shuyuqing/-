import math,os
import numpy as np


def zhenggui(path_2):#先正规化之后再打标签

    tezheng_1 = np.loadtxt(path_2, delimiter=',')

    tezheng_1 = np.transpose(tezheng_1)  # 为了方便计算，先转置

    N = tezheng_1.shape[1]

    # print(tezheng_1)
    # print(tezheng_1.shape)

    # os.system('pause')

    zhenggui_list = []

    for d in tezheng_1:

        zhenggui_list_1 = []

        pingfanghe = 0

        for d_1 in d:

            pingfanghe += math.pow(d_1,2)

        xishu =math.sqrt(N/pingfanghe)

        # print(pingfanghe)
        # print(xishu)

        for u in d:

            zhenggui_list_1.append(u*xishu)

        zhenggui_list.append(zhenggui_list_1)

    zhenggui_list_2 = np.array(zhenggui_list)

    zhenggui_list_2 = np.transpose(zhenggui_list_2)  # 为了方便计算，先转置

    # np.savetxt(path_2+"zhenggui"+'_'+ ".csv", zhenggui_list_2, delimiter=',')

    return zhenggui_list_2

# zhenggui(path_2 = r'C:\Users\a7825\Desktop\工作空间\セミナー\语音\wav/C001L_061.wav.csv')
