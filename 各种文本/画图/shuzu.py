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
log = logfbank(x, fs, nfilt=40)

np.savetxt(indir + ".csv", log, delimiter=',')

ig, ax = plt.subplots()
log= np.swapaxes(log, 0 ,1)
cax = ax.imshow(log, interpolation='nearest', origin='lower', aspect='auto')


plt.show() 
