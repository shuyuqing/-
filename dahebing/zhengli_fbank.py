from shutil import copyfile
import os
import muluzai
import numpy as np

fenshu = 5#这里的5是全部数据的五分之一作为测试数据

def zhengli(path,guanjianzi_1,dataname_1,dataname_2):

    if len(dataname_1) > len(dataname_2):

        dataname = dataname_1

    else:

        dataname = dataname_2

    path_data = os.path.join(path,dataname)
    muluzai.mkdir(path_data)

    path_fbank = os.path.join(path_data,'fbank')
    muluzai.mkdir(path_fbank)

    path_fbank_all = os.path.join(path_fbank,'all')
    path_fbank_opentest = os.path.join(path_fbank,'opentest')
    path_fbank_closetest = os.path.join(path_fbank,'closetest')
    path_fbank_xuexi = os.path.join(path_fbank,'xuexi')

    muluzai.mkdir(path_fbank_all)
    muluzai.mkdir(path_fbank_opentest)
    muluzai.mkdir(path_fbank_closetest)
    muluzai.mkdir(path_fbank_xuexi)

    for wenjian in os.listdir(path):

        if wenjian != dataname:
            path_1 = os.path.join(path,wenjian)
            path_2 = os.path.join(path_1,guanjianzi_1)

            #这个部分是fbank的部分
            for u in os.listdir(path_2):
                copyfile(os.path.join(path_2,u), os.path.join(path_fbank_all,u))  # 自动复制

            wenjian_fbank_all = os.listdir(path_2)

            wenjian_fbank_open = []
            wenjian_fbank_xuexi = []

            perm = np.random.permutation(len(wenjian_fbank_all))#随机生成size跟文件数量相等的列表

            perm_1 = perm[:int(len(wenjian_fbank_all)/fenshu)]#这里的5是全部数据的五分之一作为测试数据
            for a in perm_1:
                wenjian_fbank_open.append(wenjian_fbank_all[a])

            perm_2 = perm[int(len(wenjian_fbank_all)/fenshu):]#剩下的五分之四是学习数据
            for i in perm_2:
                wenjian_fbank_xuexi.append(wenjian_fbank_all[i])

            wenjian_fbank_close = wenjian_fbank_xuexi[:int(len(wenjian_fbank_all)/fenshu)]#学习数据里面的一部分是闭测的数据

            # wenjian_fbank_open = wenjian_fbank_all[perm[:int(len(wenjian_fbank_all)/fenshu)]]
            # wenjian_fbank_xuexi = wenjian_fbank_all[int(len(wenjian_fbank_all)/fenshu):]#剩下的五分之四是学习数据
            # wenjian_fbank_close = wenjian_fbank_xuexi[:int(len(wenjian_fbank_all)/fenshu)]#学习数据里面的一部分是闭测的数据

            for u in wenjian_fbank_close:
                copyfile(os.path.join(path_2,u),os.path.join(path_fbank_closetest,u))
            for u in wenjian_fbank_xuexi:
                copyfile(os.path.join(path_2,u),os.path.join(path_fbank_xuexi,u))
            for u in wenjian_fbank_open:
                copyfile(os.path.join(path_2,u),os.path.join(path_fbank_opentest,u))
