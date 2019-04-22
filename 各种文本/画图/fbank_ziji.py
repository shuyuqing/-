#显示波形图等各种图
import matplotlib.pyplot as plt
import librosa as li
import librosa.display as ds
import librosa
from python_speech_features.base import mfcc,logfbank
import scipy.io.wavfile as wav
import numpy as np
import os

indir = r'C:\Users\a7825\Desktop\工作空间\セミナー\语音\wav/C001L_061.wav'
# indir_1 =r'C:\Users\a7825\Desktop\工作空间\杂物\临时\这个就对了'

# 显示メルフィルタバンク的图
x, fs = li.load(indir,sr=16000)
# (fs, x) = wav.read(indir)
log = logfbank(x, fs)

# np.savetxt(indir_1 + ".csv", log, delimiter=',')
# print(log.shape)
# os.system('pause')

# for e in range(11,21):
#     for i in range(26):
#         log[e][i] = log[e][i]+3.5#为了让图变得亮一点

# ig, ax = plt.subplots()
# plt.xlim(0,130)#设置x的范围
plt.ylim(0,25.6)#设置y的范围

# new_ticks = np.linspace(0.00,5.00,4)
# plt.xticks(new_ticks)
# 设置x轴的取值


plt.xticks([0,20,40,60,80,100,120],['0.0','0.2','0.4','0.6','0.8','1.0','1.2'])
# plt.yticks([0,6.25,12.5,18.75,25],[0,2000,4000,6000,8000])
# 把x轴显示的数字都换掉，当然，y也可以这么去换
log= np.swapaxes(log, 0 ,1)
plt.imshow(log, interpolation='None', origin='lower', aspect='auto')
# plt.set_title('fbank')
plt.xlabel('Time(s)')
plt.ylabel('Filterbank #indexes')
# plt.ylabel('Frequency(Hz)')
plt.show()
# plt.plot(log)
# plt.show()