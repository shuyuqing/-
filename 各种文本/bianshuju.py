import os
import numpy as np
import muluzai as mulu

def bianshuju(path,weidu,guanjianzi):

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

                print(X_train)

                os.system('pause')

            if X_train_1 is None:
                X_train_1, Y_train_1 = X_train, Y_train
            else:
                X_train_1, Y_train_1 = np.concatenate((X_train_1, X_train), 0), np.concatenate((Y_train_1, Y_train), 0)

        np.savez(save_dir, X_train_1, Y_train_1)  # 把矩阵保存成npz文件

bianshuju(path=r'C:\Users\a7825\Desktop\新建文件夹\新建文件夹', weidu = 40, guanjianzi='mizhichuli_biaoqian_pingheng')
