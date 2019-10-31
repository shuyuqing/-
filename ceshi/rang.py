# for i in range(3):
#     print(i)

import os
import numpy as np
import muluzai as mulu


def bianshuju(path,weidu,guanjianzi,guanjianzi_1):

    for mulu in os.listdir(path):#每个循环要打开一个大文件，C064L，C064R...

        input_dir = os.path.join(path, mulu, guanjianzi)#装特征值的文件夹的地址

        save_path = os.path.join(input_dir, guanjianzi_1)#转换之后的数据都放在这个文件夹里面

        mulu.mkdir(save_path)

        for tezhenzhi in os.listdir(input_dir):#每个循环要处理一个特征值文件

            input_dir_1 = os.path.join(input_dir,tezhenzhi)#特征值的地址

            print(input_dir_1)

            f = open(input_dir_1, 'r')
            a = np.loadtxt(f, delimiter=',', skiprows=0, )

            X = a[:, 1:None]
            label = a[:, 0:1]

            cishu = int((X.shape[1])/weidu)#

            save_path_1 = os.path.join(save_path, tezhenzhi)#block序号还没有加上去的特征值的地址(转化之后)

            block_index = 1#每个文件会产生很多个block,这个是block序号

            for xinhao in X:#每一循环产生一个大block的数据,每一个大block作为一个单独的数据保存

                banyun = []
                start = 0

                for cishu_1 in range(weidu):#每一次循环产生一次傅里叶变换的结果

                    print(xinhao[start:start+cishu])

                    banyun.append(xinhao[start:start+cishu])

                    start = start+cishu

                (filepath, tempfilename) = os.path.split(save_path_1)#为了得到带序号的路径

                save_path_2 = os.path.join(filepath+'_'+ str(block_index) + '.csv')

                np.savez(normalized_feat_file, X_train, Y_train, X_test, Y_test)  # 把矩阵保存成npz文件

                # np.savetxt(, newtezheng, delimiter=',')

                banyun = np.array(banyun)

                block_index += 1

                print(banyun)

                print(banyun.shape)

                os.system('pause')



bianshuju(path=r'C:\Users\a7825\Desktop\新建文件夹\新建文件夹', weidu = 40, guanjianzi='mizhichuli_biaoqian_pingheng', guanjianzi_1='bianshuju')