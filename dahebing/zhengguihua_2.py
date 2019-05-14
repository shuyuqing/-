import math,os
import numpy as np
import muluzai as mu

def zhenggui(path,guanjianzi,guanjianzi_1):#先正规化之后再打标签

    for wenjianming in os.listdir(path):

        path_1 = os.path.join(path, wenjianming, guanjianzi)

        path_new = os.path.join(path, wenjianming, guanjianzi + '_'+guanjianzi_1)

        mu.mkdir(path_new)

        for wenjian in os.listdir(path_1):

            path_2 = os.path.join(path_1,wenjian)

            tezheng_1 = np.loadtxt(path_2, delimiter=',')

            tezheng_1 = np.transpose(tezheng_1)#为了方便计算，先转置


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

            # print(zhenggui_list_2)

            # print(zhenggui_list_2)

            np.savetxt(path_new + "/" + wenjian, zhenggui_list_2,delimiter=',')


# zhenggui(path = r'C:\Users\a7825\Desktop\新建文件夹 (4)',guanjianzi ='log' )