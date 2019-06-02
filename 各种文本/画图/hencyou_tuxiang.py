#把从语音文件中提取特征值转变成很雀死白裤托落
import numpy as np
import numpy.fft as nf
import scipy.fftpack as sc
#numpy跟scipy都提供了fft这个函数
import os
import math as ma
import muluzai as mulu
from python_speech_features.base import mfcc,fbank,logfbank
import scipy.io.wavfile as wav
import zhengguihua as zg
import matplotlib.pyplot as plt



basedir = r'C:\Users\a7825\Desktop\工作空间\セミナー\语音\wav/C001L_007.wav'
start = 0
block = 32#窗口范围是1到32帧
weidu = 40

def mizhichuli(basedir,block,weidu):

    (fs, audio) = wav.read(basedir)
    log = logfbank(audio, fs, nfilt=weidu)
    np.savetxt(basedir + ".logfbank" + ".csv", log, delimiter=',')

    tezheng = np.loadtxt(basedir + ".logfbank" + ".csv", delimiter=',')
    tezheng = np.array(tezheng,float)

    tezheng_3 = tezheng[start:block]#把前32帧数据取出来

    tezheng_3 = np.array(tezheng_3, float)

    print(tezheng_3)
    print(tezheng_3.shape)
    print('分割')

    tezheng_3 = np.transpose(tezheng_3)

    print(tezheng_3)
    print(tezheng_3.shape)
    print('分割')

    tezheng_5 = []


    #以下是正规化
    for m in tezheng_3:#一列列去正规化

        zheng = zg.zhenggui(m,block)

        print(zheng)
        print('分割')

        tezheng_5.append(zheng)

    tezheng_5 = np.array(tezheng_5)
    #以上是正规化

    #以下是非正规化
    # tezheng_5 = np.array(tezheng_3)
    #以上是非正规化




    q = int(block / 2)  # 把需要正规化的数据取出来

    tezheng_7 = []

    for o in tezheng_5:

        print(o)
        print('以上是0_2')
        o_2 = nf.fft(o)
        print(o_2)
        print('以上是傅里叶变换后的o_2')

        tezheng_6 = []

        for n in range(q, block):  # 之前括号里面的值是block,因为要扔掉一半所以改了

            fft = ma.sqrt(ma.pow(o_2[n].imag, 2) + ma.pow(o_2[n].real, 2))
            print(fft)
            print("分割")
            # os.system('pause')
            tezheng_6.append(fft)

        print(tezheng_6)
        print('以上是tezheng_6')

        tezheng_7.append(tezheng_6)



    tezheng_7 = np.array(tezheng_7)
    tezheng_7 = np.transpose(tezheng_7)

    print(tezheng_7)
    print("以上是tezheng_7")
    print(tezheng_7.shape)

    #以上是对一个block进行正规化之后再henncyou的结果

    ig, ax = plt.subplots()
    log = np.swapaxes(tezheng_7, 0, 1)
    cax = ax.imshow(log, interpolation='nearest', origin='lower', aspect='auto')

    # plt.xticks([0, 20, 40, 60, 80, 100], ['0', '10', '20', '30', '40', '50'])
    plt.yticks([0, 5, 10, 15, 20, 25, 30, 35, 39.5], ['0', '5', '10', '15', '20', '25', '30', '35', '40'])

    plt.xlabel('Modulation frequency(Hz)')
    plt.ylabel('Filterbank index')

    plt.show()


if __name__ == '__main__':

    mizhichuli(basedir,block,weidu)