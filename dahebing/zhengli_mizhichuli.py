from shutil import copyfile
import os
import muluzai
import numpy as np

fenshu = 5#这里的5是全部数据的五分之一作为测试数据

def zhengli(path,guanjianzi_2,dataname_1,dataname_2):

    if len(dataname_1) > len(dataname_2):

        dataname = dataname_1

    else:

        dataname = dataname_2

    path_data = os.path.join(path,dataname)
    muluzai.mkdir(path_data)

    path_mizhichuli = os.path.join(path_data,'mizhichuli')
    muluzai.mkdir(path_mizhichuli)

    path_mizhichuli_all = os.path.join(path_mizhichuli,'all')
    path_mizhichuli_opentest = os.path.join(path_mizhichuli,'opentest')
    path_mizhichuli_closetest = os.path.join(path_mizhichuli,'closetest')
    path_mizhichuli_xuexi = os.path.join(path_mizhichuli,'xuexi')

    muluzai.mkdir(path_mizhichuli_all)
    muluzai.mkdir(path_mizhichuli_opentest)
    muluzai.mkdir(path_mizhichuli_closetest)
    muluzai.mkdir(path_mizhichuli_xuexi)

    for wenjian in os.listdir(path):

        if wenjian != dataname:
            path_1 = os.path.join(path,wenjian)
            path_3 = os.path.join(path_1,guanjianzi_2)

            #这个部分是mizhichuli的部分
            for i in os.listdir(path_3):
                copyfile(os.path.join(path_3,i), os.path.join(path_mizhichuli_all,i))

            wenjian_mizhichuli_all = os.listdir(path_3)

            wenjian_mizhichuli_open = []
            wenjian_mizhichuli_xuexi = []

            perm = np.random.permutation(len(wenjian_mizhichuli_all))#随机生成size跟文件数量相等的列表

            perm_1 = perm[:int(len(wenjian_mizhichuli_all) / fenshu)]  # 这里的5是全部数据的五分之一作为测试数据
            for a in perm_1:
                wenjian_mizhichuli_open.append(wenjian_mizhichuli_all[a])

            perm_2 = perm[int(len(wenjian_mizhichuli_all) / fenshu):]  # 剩下的五分之四是学习数据
            for i in perm_2:
                wenjian_mizhichuli_xuexi.append(wenjian_mizhichuli_all[i])

            wenjian_mizhichuli_close = wenjian_mizhichuli_xuexi[:int(len(wenjian_mizhichuli_all) / fenshu)]  # 学习数据里面的一部分是闭测的数据

            # wenjian_mizhichuli_open = wenjian_mizhichuli_all[:int(len(wenjian_mizhichuli_all)/5)]#这里的5是全部数据的五分之一作为测试数据
            # wenjian_mizhichuli_xuexi = wenjian_mizhichuli_all[int(len(wenjian_mizhichuli_all)/5):]
            # wenjian_mizhichuli_close = wenjian_mizhichuli_xuexi[:int(len(wenjian_mizhichuli_all)/5)]

            for u in wenjian_mizhichuli_close:
                copyfile(os.path.join(path_3,u),os.path.join(path_mizhichuli_closetest,u))
            for u in wenjian_mizhichuli_xuexi:
                copyfile(os.path.join(path_3,u),os.path.join(path_mizhichuli_xuexi,u))
            for u in wenjian_mizhichuli_open:
                copyfile(os.path.join(path_3,u),os.path.join(path_mizhichuli_opentest,u))