from shutil import copyfile
import os
import muluzai
import numpy as np

def zhengli(path,guanjianzi_2,dataname_1,dataname_2,guanjianzi_3):

    if len(dataname_1) > len(dataname_2):

        dataname = dataname_1

    else:

        dataname = dataname_2

    path_data = os.path.join(path,dataname)
    muluzai.mkdir(path_data)

    path_mizhichuli = os.path.join(path_data,'mizhichuli')
    muluzai.mkdir(path_mizhichuli)

    path_mizhichuli_all = os.path.join(path_mizhichuli,'all',guanjianzi_3)

    muluzai.mkdir(path_mizhichuli_all)

    for wenjian in os.listdir(path):

        if wenjian != dataname:
            path_1 = os.path.join(path,wenjian)
            path_3 = os.path.join(path_1,guanjianzi_2)

            #这个部分是mizhichuli的部分
            for i in os.listdir(path_3):
                copyfile(os.path.join(path_3,i), os.path.join(path_mizhichuli_all,i))
