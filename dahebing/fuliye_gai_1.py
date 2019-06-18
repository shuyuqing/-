# 把从语音文件中提取特征值转变成很雀死白裤托落
import numpy as np
import numpy.fft as nf
import scipy.fftpack as sc
# numpy跟scipy都提供了fft这个函数
import os,math
import math as ma
import muluzai as mulu
import jiachuang as jc


def mizhichuli(basedir,chuangkou,padding,lintianchong):

    jiachuang = True
    bulin = 'log_qian5'
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
            block = chuangkou
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

                N = block

                for m in range(huishu):

                    # print(tezheng_1[start:end])

                    #正规化部分

                    zhenggui_list_1 = []

                    pingfanghe = 0

                    # print(tezheng_1)

                    for d in tezheng_1[start:end]:

                        # print(d)
                        pingfanghe += math.pow(d, 2)

                        # print(pingfanghe)
                        # print(xishu)

                    xishu = math.sqrt(N / pingfanghe)

                    for u in tezheng_1[start:end]:

                        zhenggui_list_1.append(u * xishu)

                    zhenggui_list_1 = np.array(zhenggui_list_1)

                    if lintianchong == True:#如果要进行零填充，这个变量就要设置为True

                        # print(zhenggui_list_1)
                        # os.system('pause')

                        lin = np.zeros(padding)#进行零补充
                        zhenggui_list_1 = np.hstack((zhenggui_list_1, lin))

                        # print(zhenggui_list_1)
                        # os.system('pause')
                    if jiachuang == True:

                        zhenggui_list_1 = jc.jiachuangzi(zhenggui_list_1)

                    tezheng_2 = nf.fft(zhenggui_list_1)

                    # print(tezheng_2)
                    # print("第%d列的第%d波"%(i,m))
                    # print(tezheng_2)
                    block_1 = block + padding
                    # print('输出block')
                    # print(block_1)

                    q = int(block_1 / 2)
                    # for n in range(q, block_1):  # 之前括号里面的值是block_1,因为要扔掉一半所以改了
                    for n in range(0, q):  # 要取前半部分

                        zhongzhuan = []
                        zhongzhuan.append(ma.sqrt(ma.pow(tezheng_2[n].imag, 2) + ma.pow(tezheng_2[n].real, 2)))
                        tezheng_3[m].extend(zhongzhuan)

                    # print(tezheng_3)
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
