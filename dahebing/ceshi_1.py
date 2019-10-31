#提取各种特征值
import scipy.io.wavfile as wav
from python_speech_features.base import mfcc,fbank,logfbank
import numpy as np
import os
import muluzai as muluz


(fs, audio) = wav.read(r'C:\Users\a7825\Desktop\新建文件夹\新建文件夹\C1_F_05\wav/l_289220_295510_C1_F_05.wav')




# tiqu(path=r'C:\Users\a7825\Desktop\新建文件夹 (4)',weidu=26,logenergy=False,energy_1=True)
