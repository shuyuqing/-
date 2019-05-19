#显示波形图等各种图
import matplotlib.pyplot as plt
import librosa as li
import librosa.display as ds
import librosa
from python_speech_features.base import mfcc,logfbank,fbank
import scipy.io.wavfile as wav
import numpy as np
import zhengguihua
import os

indir = r'C:\Users\a7825\Desktop\工作空间\セミナー\语音\wav/C001L_061.wav'
# indir_1 =r'C:\Users\a7825\Desktop\工作空间\杂物\临时\这个就对了'

# 显示logメルフィルタバンク的图
(fs, x) = wav.read(indir)
log = logfbank(x, fs)

# np.savetxt(indir_1 + ".csv", log, delimiter=',')

ig, ax = plt.subplots()
# log= np.swapaxes(log, 0 ,1)
cax = ax.imshow(log, interpolation='nearest', origin='lower', aspect='auto')


ax.set_title('fbank')
plt.show()
plt.plot(log)
plt.show()

# 显示メルフィルタバンク的图
# x, fs = li.load(indir,sr=16000)
(fs, x) = wav.read(indir)
log,energy = fbank(x, fs)

# np.savetxt(indir_1 + ".csv", log, delimiter=',')

ig, ax = plt.subplots()
# log= np.swapaxes(log, 0 ,1)
cax = ax.imshow(log, interpolation='nearest', origin='lower', aspect='auto')


ax.set_title('fbank')
plt.show()
plt.plot(log)
plt.show()







# librosa.display.specshow(log, y_axis='mel', x_axis='time')
# plt.xlim(0,0.32)#设置x的范围
# plt.ylim(0,15)#设置y的范围
# new_ticks = np.linspace(0.00,5.00,4)
# plt.xticks(new_ticks)
# 设置x轴的取值
# plt.xticks([0,1,2,3,4,5],['0.00','1.00','2.00','3.00','4.00','5.00'])
# 把x轴显示的数字都换掉，当然，y也可以这么去换
# plt.show()




#现实波形图
# x, fs = li.load(indir,sr=16000,duration=0.32)
# x, fs = li.load(indir,sr=16000)
# ds.waveplot(x, sr=fs, x_axis='time',color='blue')
# librosa.feature.melspectrogram(y=x, sr=fs)
# plt.xticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1],['0','10','20','30','40','50','60','70','80','90','100','110'])
# plt.title('wave')
# plt.show()

#显示mfcc的图
# mfccs = librosa.feature.mfcc(x, sr=fs)
# librosa.display.specshow(mfccs, sr=fs, x_axis='time')
# plt.colorbar()

# 显示spectrogram的图像
# x, fs = li.load(indir,sr=16000,duration=0.32)
# # (fs, x) = wav.read(indir)
# # log = logfbank(x, fs)
# spe = librosa.feature.melspectrogram(y=x,sr=fs)
# ig, ax = plt.subplots()
# mfcc_data= np.swapaxes(spe, 0 ,1)
# cax = ax.imshow(mfcc_data, interpolation='nearest', origin='lower', aspect='auto')
# ax.set_title('spectrogram')
# plt.show()
# plt.plot(spe)
# plt.show()

#fbank正规化之后的图
# (fs, x) = wav.read(indir)
# feat,energy = fbank(x, fs)
#
# np.savetxt(indir+'_sc_' + ".csv", feat, delimiter=',')
#
# path = indir+'_sc_' + ".csv"
#
# log_zhenggui = zhengguihua.zhenggui(path)
#
#
#
# ig, ax = plt.subplots()
# # log_zhenggui= np.swapaxes(log_zhenggui, 0 ,1)
# cax = ax.imshow(log_zhenggui, interpolation='nearest', origin='lower', aspect='auto')
#
#
# ax.set_title('fbank')
# plt.show()
# plt.plot(log)
# plt.show()