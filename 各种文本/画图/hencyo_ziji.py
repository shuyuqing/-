#显示変動スベクトル的图
import matplotlib.pyplot as plt
import librosa as li
import librosa.display as ds
import librosa
from python_speech_features.base import mfcc,logfbank
import scipy.io.wavfile as wav
import numpy as np

#把从语音文件中提取特征值转变成很雀死白裤托落
import numpy as np
import numpy.fft as nf
import scipy.fftpack as sc
#numpy跟scipy都提供了fft这个函数
import os
import math as ma
import  csv
if __name__ == '__main__':

    indir = r'C:\Users\a7825\Desktop\工作空间\セミナー\语音\mizhichuli_log/C001L_061.wav.csv'
    #
    # banyun = []
    # banyun_2 = []
    # newtezheng = csv.reader(indir)
    newtezheng = np.loadtxt(indir, delimiter=',', skiprows=0).astype(np.float32)
    # for i in newtezheng:
    #     for y in i:
    #         banyun.append(float(y))
    #     banyun_2.append(banyun)


    data = np.array(newtezheng, dtype=np.float32)


    data = np.swapaxes(data, 0, 1)
    # data = np.swapaxes(data, 0, 1)
    # cax = ax.imshow(data, interpolation='none', origin='lower', aspect='auto')

    plt.imshow(data, interpolation='sinc', origin='lower', aspect='auto')



    plt.xlabel('Modulation frequency(Hz)')
    plt.ylabel('Filterbank #indexs')

    # plt.xlim(0,5)#设置x的范围
    # plt.ylim(0,15)#设置y的范围

    # new_ticks = np.linspace(0.00,5.00,4)
    # plt.xticks(new_ticks)
    #设置x轴的取值


    plt.xticks([-0.5,2.5,5.5,8.5,11.5,14.5],['0','10','20','30','40','50'])
    #把x轴显示的数字都换掉，当然，y也可以这么去换

    plt.show()
    # plt.plot(log)
    # plt.show()

