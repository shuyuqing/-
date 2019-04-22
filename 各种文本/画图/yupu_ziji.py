import wave
import matplotlib.pyplot as plt
import numpy as np
import os
#显示波形图等各种图
import matplotlib.pyplot as plt
import librosa as li
import librosa.display as ds
import librosa
from python_speech_features.base import mfcc,logfbank
import scipy.io.wavfile as wav
import numpy as np
import scipy.signal as ss

# filepath = r"C:\Users\a7825\Desktop\新しいフォルダー/"  # 添加路径
# filename = os.listdir(filepath)  # 得到文件夹下的所有文件名称
# f = wave.open(filepath + filename[0], 'rb')
indir = r'C:\Users\a7825\Desktop\工作空间\语音数据\UUDB\第一次实验/C001L_065.wav'

x, fs = li.load(indir,sr=16000)
# # (fs, x) = wav.read(indir)
#
plt.specgram(x, Fs=fs, scale_by_freq=True, sides='onesided',NFFT=512)
plt.ylabel('Frequency(Hz)')
plt.xlabel('Time(s)')
plt.show()


# fs,time,data = ss.spectrogram(x,fs = fs,window=('tukey', 0.25), nfft=512,mode='magnitude')
#


# log = logfbank(x, fs)
# plt.imshow(spectro, interpolation='nearest', origin='lower', aspect='auto')
# # plt.set_title('fbank')
# plt.show()

