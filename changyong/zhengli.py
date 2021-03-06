from shutil import copyfile
import os
import muluzai
import numpy as np

path = r'C:\Users\a7825\Desktop\工作空间\杂物\对比'
fenshu = 5#这里的5是全部数据的五分之一作为测试数据

def zhengli(path):

    path_data = os.path.join(path,'data')
    muluzai.mkdir(path_data)

    path_fbank = os.path.join(path_data,'fbank')
    path_mizhichuli = os.path.join(path_data,'muzhichuli')
    muluzai.mkdir(path_fbank)
    muluzai.mkdir(path_mizhichuli)

    path_fbank_all = os.path.join(path_fbank,'all')
    path_fbank_opentest = os.path.join(path_fbank,'opentest')
    path_fbank_closetest = os.path.join(path_fbank,'closetest')
    path_fbank_xuexi = os.path.join(path_fbank,'xuexi')

    path_mizhichuli_all = os.path.join(path_mizhichuli,'all')
    path_mizhichuli_opentest = os.path.join(path_mizhichuli,'opentest')
    path_mizhichuli_closetest = os.path.join(path_mizhichuli,'closetest')
    path_mizhichuli_xuexi = os.path.join(path_mizhichuli,'xuexi')

    muluzai.mkdir(path_fbank_all)
    muluzai.mkdir(path_fbank_opentest)
    muluzai.mkdir(path_fbank_closetest)
    muluzai.mkdir(path_fbank_xuexi)

    muluzai.mkdir(path_mizhichuli_all)
    muluzai.mkdir(path_mizhichuli_opentest)
    muluzai.mkdir(path_mizhichuli_closetest)
    muluzai.mkdir(path_mizhichuli_xuexi)

    for wenjian in os.listdir(path):

        if wenjian != 'data':
            path_1 = os.path.join(path,wenjian)
            path_2 = os.path.join(path_1,'xinde_log')
            path_3 = os.path.join(path_1,'xinde_mizhichuli')

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

            #这个部分是mizhichuli的部分
            for i in os.listdir(path_3):
                copyfile(os.path.join(path_3,i), os.path.join(path_mizhichuli_all,i))

            wenjian_mizhichuli_all = os.listdir(path_3)

            wenjian_mizhichuli_open = []
            wenjian_mizhichuli_xuexi = []

            perm = np.random.permutation(len(wenjian_mizhichuli_all))  # 随机生成size跟文件数量相等的列表

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
