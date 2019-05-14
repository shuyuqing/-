# 把从语音文件中提取特征值转变成很雀死白裤托落
import numpy as np
import numpy.fft as nf
import scipy.fftpack as sc
# numpy跟scipy都提供了fft这个函数
import os
import math as ma
import muluzai as mulu

def mizhichuli(basedir):

    bulin = 'bulin'

    mizhichuli_log = 'mizhichuli'

    for mulu_1 in os.listdir(basedir):
        lujing = os.path.join(basedir, mulu_1, mizhichuli_log)
        # 处理之后的特征值文件应该存放的地方
        filepath = os.path.join(basedir, mulu_1, bulin)
        # 需要被处理的特征值文件

        mulu.mkdir(lujing)

        for name in os.listdir(filepath):

            file_path = os.path.join(filepath, name)
            final_path = os.path.join(lujing, name.replace('.log', ''))

            tezheng = np.loadtxt(file_path, delimiter=',')
            tezheng = np.array(tezheng, float)

            hang = tezheng.shape[0]
            lie = tezheng.shape[1]

            # 获得特征值矩阵的行数和列数

            newtezheng = []

            global block, start, end, huishu
            start = 0
            block = 32
            # block是窗口的大小
            huishu = hang - block + 1
            # 每一列要做的傅里叶变化的次数

            end = block

            tezheng_3 = [[] for row in range(huishu)]
            # print(len(tezheng_3))

            for i in range(lie):
                # print("现在处理第%d列"%i)
                start = 0
                end = block
                tezheng_1 = np.loadtxt(file_path, delimiter=',', usecols=(i))
                # 一列一列第取出数据，usecols起到了这个作用

                for m in range(huishu):

                    # print(tezheng_1[start:end])
                    tezheng_2 = nf.fft(tezheng_1[start:end])

                    # print("第%d列的第%d波"%(i,m))
                    # print(tezheng_2)
                    q = int(block / 2)
                    for n in range(q, block):  # 之前括号里面的值是block,因为要扔掉一半所以改了
                        zhongzhuan = []
                        zhongzhuan.append(ma.sqrt(ma.pow(tezheng_2[n].imag, 2) + ma.pow(tezheng_2[n].real, 2)))
                        tezheng_3[m].extend(zhongzhuan)
                        # tezheng_3 = ma.sqrt(ma.pow(tezheng_2[n].imag,2)+ma.pow(tezheng_2[n].real,2))
                    # print(tezheng_3)
                    # print("新的特征值")
                    # print(tezheng_3[m])
                    # print('下一波')
                    start = start + 1
                    end = end + 1

            newtezheng = np.array(tezheng_3, dtype=np.float)
            # newtezheng = np.transpose(newtezheng)
            np.savetxt(final_path, newtezheng, delimiter=',')