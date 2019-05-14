import math,os
import numpy as np
import muluzai as mu

def zhenggui(path,guanjianzi):#先正规化之后再打标签

    for wenjianming in os.listdir(path):

        path_1 = os.path.join(path, wenjianming, guanjianzi)

        path_new = os.path.join(path, wenjianming, guanjianzi + '_zhengguihua')

        mu.mkdir(path_new)

        for wenjian in os.listdir(path_1):

            path_2 = os.path.join(path_1,wenjian)

            tezheng_1 = np.loadtxt(path_2, delimiter=',')

            tezheng_1 = np.transpose(tezheng_1)#为了方便计算，先转置

            # print(tezheng_1)
            # print(tezheng_1.shape)
            #
            # print(tezheng_1[0])
            # print(tezheng_1[1])

            zhenggui_list_1 = []

            for d in tezheng_1:

                heji=0

                for u in d:

                    heji += math.pow(u,2)

                scale = math.sqrt(heji)

                zhenggui_list = []

                for u in d:

                    u_1 = u/scale
                    zhenggui_list.append(u_1)

                zhenggui_list_1.append(zhenggui_list)

            zhenggui_list_2 = np.array(zhenggui_list_1)

            zhenggui_list_2 = np.transpose(zhenggui_list_2)

            # print(zhenggui_list_2)

            np.savetxt(path_new + "/" + wenjian, zhenggui_list_2,delimiter=',')

















# zhenggui(path = r'C:\Users\a7825\Desktop\新建文件夹 (4)',guanjianzi ='log' )