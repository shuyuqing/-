import os
import numpy as np
import muluzai as mulu

def bianshuju(path,weidu,guanjianzi):#把之前立起来的变调还原并保存为npz格式

    for mulu in os.listdir(path):#每个循环要打开一个大文件，C064L，C064R...

        input_dir = os.path.join(path, mulu, guanjianzi)#装特征值的文件夹的地址
        save_dir = os.path.join(path, mulu, mulu + '.npz' )

        X_train_1 = None
        Y_train_1 = None

        for tezhenzhi in os.listdir(input_dir):#每个循环要处理一个特征值文件

            input_dir_1 = os.path.join(input_dir,tezhenzhi)#特征值的地址

            print(input_dir_1)

            f = open(input_dir_1, 'r')
            a = np.loadtxt(f, delimiter=',', skiprows=0, )

            X = a[:, 1:None]
            Y_train = a[:, 0:1]

            cishu = int((X.shape[1])/weidu)

            X_train = None

            for xinhao in X:#每一循环产生一个大block的数据,每一个大block作为一个单独的数据保存

                banyun = []
                start = 0

                for cishu_1 in range(weidu):#每一次循环产生一次傅里叶变换的结果

                    banyun.append(xinhao[start:start+cishu])

                    start = start+cishu

                banyun = np.array(banyun)

                if X_train is None:
                    X_train = banyun
                else:
                    X_train = np.concatenate((X_train, banyun), 0)


            if X_train_1 is None:
                X_train_1, Y_train_1 = X_train, Y_train
            else:
                X_train_1, Y_train_1 = np.concatenate((X_train_1, X_train), 0), np.concatenate((Y_train_1, Y_train), 0)

        np.savez(save_dir, X_train_1, Y_train_1)  # 把矩阵保存成npz文件

def hebing(path):#把大目录下的npz文件都合并到一块去(数据已经被分为test和train)

    X_train = None
    Y_train = None

    for mulu in os.listdir(path):#每个循环要打开一个大文件，C064L，C064R...

        dir = os.path.join(path, mulu, mulu + '.npz' )
        dmp = np.load(dir)
        tmp_mbe, tmp_label = dmp['arr_0'], dmp['arr_1']

        if X_train is None:
            X_train, Y_train = tmp_mbe, tmp_label
        else:
            X_train, Y_train = np.concatenate((X_train, tmp_mbe), 0), np.concatenate((Y_train, tmp_label), 0)

    save_dir = os.path.join(path, mulu, mulu + '.npz')

def hebing_1(path,weidu):#把已经整理好的学习数据和训练数据做成npz格式(数据没有被分成test和train)

    dir_train = os.path.join(path,'train','mizhichuli','all')
    dir_test = os.path.join(path,'test','mizhichuli','all')
    dir_train_save = os.path.join(path, 'train.npz')
    dir_test_save = os.path.join(path,'test.npz')

    X_train_1 = None
    Y_train_1 = None
    for tezhenzhi in os.listdir(dir_train):  # 每个循环要处理一个特征值文件
        input_dir_1 = os.path.join(dir_train, tezhenzhi)  # 特征值的地址
        print(input_dir_1)
        f = open(input_dir_1, 'r')
        a = np.loadtxt(f, delimiter=',', skiprows=0, )
        X = a[:, 1:None]
        Y_train = a[:, 0:1]
        cishu = int((X.shape[1]) / weidu)
        X_train = None
        for xinhao in X:  # 每一循环产生一个大block的数据,每一个大block作为一个单独的数据保存
            banyun = []
            start = 0
            for cishu_1 in range(weidu):  # 每一次循环产生一次傅里叶变换的结果
                banyun.append(xinhao[start:start + cishu])
                start = start + cishu
            if X_train is None:
                X_train = banyun
            else:
                X_train = np.concatenate((X_train, banyun), 1)

        # print(X_train.shape)
        X_train = np.transpose(X_train)
        # print(X_train.shape)
        # print(X_train)
        # os.system('pause')
        if X_train_1 is None:
            X_train_1, Y_train_1 = X_train, Y_train
        else:
            X_train_1, Y_train_1 = np.concatenate((X_train_1, X_train), 0), np.concatenate((Y_train_1, Y_train), 0)

        # print(X_train_1.shape)
        # os.system('pause')

    # X_train_1 = np.transpose(X_train_1)
    # print(X_train_1.shape)
    # print(Y_train_1.shape)
    # os.system('pause')
    np.savez(dir_train_save, X_train_1, Y_train_1)  # 把矩阵保存成npz文件


    X_train_1 = None
    Y_train_1 = None
    for tezhenzhi in os.listdir(dir_test):  # 每个循环要处理一个特征值文件
        input_dir_1 = os.path.join(dir_test, tezhenzhi)  # 特征值的地址
        print(input_dir_1)
        f = open(input_dir_1, 'r')
        a = np.loadtxt(f, delimiter=',', skiprows=0, )
        X = a[:, 1:None]
        Y_train = a[:, 0:1]
        cishu = int((X.shape[1]) / weidu)
        X_train = None
        for xinhao in X:  # 每一循环产生一个大block的数据,每一个大block作为一个单独的数据保存
            banyun = []
            start = 0
            for cishu_1 in range(weidu):  # 每一次循环产生一次傅里叶变换的结果
                banyun.append(xinhao[start:start + cishu])
                start = start + cishu
            if X_train is None:
                X_train = banyun
            else:
                X_train = np.concatenate((X_train, banyun), 1)

        X_train = np.transpose(X_train)

        if X_train_1 is None:
            X_train_1, Y_train_1 = X_train, Y_train
        else:
            X_train_1, Y_train_1 = np.concatenate((X_train_1, X_train), 0), np.concatenate((Y_train_1, Y_train), 0)

    # print(X_train_1.shape)
    # print(Y_train_1.shape)
    # os.system('pause')
    np.savez(dir_test_save, X_train_1, Y_train_1)  # 把矩阵保存成npz文件

hebing_1(path = r'C:\Users\a7825\Desktop\40_8_8',weidu = 40)

# bianshuju(path=r'C:\Users\a7825\Desktop\工作空间\桌面1\shiyan\symbol_40_8_8_biaoqian_pingheng', weidu = 40, guanjianzi='mizhichuli_biaoqian_pingheng')