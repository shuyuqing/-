import os,shutil
import muluzai as mu
import numpy as np

def kongwenjian(path,guanjianzi):#删除大小为零的文件aaa45665465

    for name in os.listdir(path):

        path_xinde_log = os.path.join(path,name,guanjianzi)

        for name_1 in os.listdir(path_xinde_log):

            path_xinde_log_1 = os.path.join(path_xinde_log,name_1)

            size = os.path.getsize(path_xinde_log_1)

            if size <= 2:

                print("大小为0的文件"+ path_xinde_log_1)
                os.remove(path_xinde_log_1)

def pingheng(path,guanjianzi):#把标签都是0的文件找出来

    liebiao = os.listdir(path)

    quanshi0= os.path.join(os.path.join(os.path.expanduser("~"), 'Desktop'),'table','quanshi0_' + guanjianzi)

    mu.mkdir(quanshi0)

    for name in liebiao:

        path_1 = os.path.join(path,name,guanjianzi)

        for name_1 in os.listdir(path_1):

            path_2 = os.path.join(path_1,name_1)

            f = open(path_2, 'r')

            print(path_2)
            a = np.loadtxt(f, delimiter=',', skiprows=0).astype(np.float32)

            Labeltrain = a[:, 0:1]
            f.close()

            if 1 not in Labeltrain:

                print("标签全是零的文件" + path_2)

                if os.path.exists(os.path.join(quanshi0, os.path.split(path_2)[1])): # 把文件名从路径中剥离出来，如果早已存在，就把它删除了，再覆盖掉

                    os.remove(os.path.join(quanshi0, os.path.split(path_2)[1]))
                    shutil.move(path_2, quanshi0)

                else:

                    shutil.move(path_2, quanshi0)

def pingheng_1(path,guanjianzi):  # 把标签都是1的文件找出来

    liebiao = os.listdir(path)

    quanshi1 = os.path.join(os.path.join(os.path.expanduser("~"), 'Desktop'), 'table','quanshi1_' + guanjianzi)

    mu.mkdir(quanshi1)

    for name in liebiao:

        path_mizhichuli = os.path.join(path, name, guanjianzi)

        for name_1 in os.listdir(path_mizhichuli):

            path_2 = os.path.join(path_mizhichuli, name_1)

            f = open(path_2, 'r')

            a = np.loadtxt(f, delimiter=',', skiprows=0).astype(np.float32)

            Labeltrain = a[:, 0:1]
            f.close()

            if 0 not in Labeltrain:
                print("标签全是1的文件" + path_2)

                if os.path.exists(os.path.join(quanshi1, os.path.split(path_2)[1])): # 把文件名从路径中剥离出来，如果早已存在，就把它删除了，再覆盖掉

                    os.remove(os.path.join(quanshi1, os.path.split(path_2)[1]))
                    shutil.move(path_2, quanshi1)

                else:

                    shutil.move(path_2, quanshi1)