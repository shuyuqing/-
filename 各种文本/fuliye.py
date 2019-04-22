import numpy as np
import numpy.fft as nf
import scipy.fftpack as sc
#numpy跟scipy都提供了fft这个函数
import os
import csv
import math as ma

def shanchuhang():

    fileme=r'FOY0201SUR1.csv'

    filebao=r'FOY0201SUR1_1.csv'

    lujing = r'C:\Users\a7825\Desktop\工作空间\杂物\一堆特征值/'

    indir = lujing+fileme

    indir_1 = lujing+filebao

    tezheng = np.loadtxt(indir, delimiter=',')

    hang = tezheng.shape[0]
    lie = tezheng.shape[1]
    #获得特征值矩阵的行数和列数

    newtezheng = []

    global block, start, end, huishu
    start = 0
    block = 4
    # block是窗口的大小
    huishu = hang-block+1
    #每一列要做的傅里叶变化的次数

    end = block

    tezheng_3 = [[] for row in range(huishu)]
    print(len(tezheng_3))

    for i in range(lie):
        print("现在处理第%d列"%i)
        start = 0
        end = block
        tezheng_1 = np.loadtxt(indir, delimiter=',', usecols=(i))
        #一列一列第取出数据，usecols起到了这个作用

        for m in range(huishu):

            print(tezheng_1[start:end])
            tezheng_2 = nf.fft(tezheng_1[start:end])
            print("第%d列的第%d波"%(i,m))
            print(tezheng_2)

            for n in range(block):
                zhongzhuan = []
                zhongzhuan.append(ma.sqrt(ma.pow(tezheng_2[n].imag,2)+ma.pow(tezheng_2[n].real,2)))
                tezheng_3[m].extend(zhongzhuan)
                # tezheng_3 = ma.sqrt(ma.pow(tezheng_2[n].imag,2)+ma.pow(tezheng_2[n].real,2))
            # print(tezheng_3)
            print("新的特征值")
            print(tezheng_3[m])
            print('下一波')
            start = start+1
            end = end+1

    newtezheng = np.array(tezheng_3,dtype=np.float)
    # newtezheng = np.transpose(newtezheng)
    np.savetxt(indir_1, newtezheng, delimiter=',')


if __name__ == '__main__':
 shanchuhang()