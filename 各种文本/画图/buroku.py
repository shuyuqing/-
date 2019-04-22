#把从语音文件中提取特征值转变成很雀死白裤托落
import numpy as np
import numpy.fft as nf
import scipy.fftpack as sc
#numpy跟scipy都提供了fft这个函数
import os
import math as ma
import muluzai as mulu

basedir = r'C:\Users\a7825\Desktop\工作空间\セミナー\语音'

bulin = 'lizi'

mizhichuli_log = 'mizhichuli_log'

filepath = os.path.join(basedir,bulin)
#需要被处理的特征值文件

lujing = os.path.join(basedir,mizhichuli_log)
#处理之后的特征值文件应该存放的地方

def mizhichuli(wenjian):

    file_path = os.path.join(filepath,wenjian)
    final_path = os.path.join(lujing,wenjian.replace('.log',''))

    tezheng = np.loadtxt(file_path, delimiter=',')
    tezheng = np.array(tezheng,float)

    hang = tezheng.shape[0]
    lie = tezheng.shape[1]

    #获得特征值矩阵的行数和列数

    newtezheng = []

    global block, start, end, huishu
    start = 0
    block = 32
    # block是窗口的大小
    huishu = 1
    #每一列要做的傅里叶变化的次数

    end = block

    tezheng_3 = []
    # print(len(tezheng_3))

    for i in range(lie):
        # print("现在处理第%d列"%i)
        start = 0
        end = block
        tezheng_1 = np.loadtxt(file_path, delimiter=',', usecols=(i))
        #一列一列第取出数据，usecols起到了这个作用

        # print('tezheng_1[:]')
        # print(tezheng_1[:])
        # os.system('pause')

        tezheng_2= nf.fft(tezheng_1[:])

        # print("tezhen_2")
        # # print("第%d列的第%d波"%(i,m))
        # print(tezheng_2)
        # os.system("pause")

        q = int(block/2)
        zhongzhuan = []

        for n in range(q,block):#之前括号里面的值是block,因为要扔掉一半所以改了

            # if n ==q+2 or n ==q+3 or n ==q+4 or n ==q+5 or n==q+6 or n==q+7:
                zhongzhuan.append(ma.sqrt(ma.pow(tezheng_2[n].imag,2)+ma.pow(tezheng_2[n].real,2))+(n-q)*5)#画图的时候更亮一点
                # zhongzhuan.append(ma.sqrt(ma.pow(tezheng_2[n].imag, 2) + ma.pow(tezheng_2[n].real, 2)))
            # else:
            #     zhongzhuan.append(ma.sqrt(ma.pow(tezheng_2[n].imag, 2) + ma.pow(tezheng_2[n].real, 2)))
            # print("zhongzhuan")
            # print(zhongzhuan)
            # os.system('pause')

        tezheng_3.append(zhongzhuan)


        # print("tezheng_3")
        # print(tezheng_3)
        # os.system("pause")
            # tezheng_3 = ma.sqrt(ma.pow(tezheng_2[n].imag,2)+ma.pow(tezheng_2[n].real,2))
        # print(tezheng_3)
        # print("新的特征值")
        # print(tezheng_3[m])
        # print('下一波')



    newtezheng = np.array(tezheng_3,dtype=np.float)
    newtezheng = np.transpose(newtezheng)
    np.savetxt(final_path, newtezheng, delimiter=',')



if __name__ == '__main__':

    mulu.mkdir(lujing)
    for name in os.listdir(filepath):
        print("正在处理文件%s"%name)
        mizhichuli(name)
