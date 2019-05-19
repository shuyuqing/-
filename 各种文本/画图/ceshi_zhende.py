import csv
import os
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
import librosa as li
import librosa.display as ds
from python_speech_features.base import mfcc,logfbank
import scipy.io.wavfile as wav
import numpy as np


input_dir = r'C:\Users\a7825\Desktop\新建文件夹 (4)\C1_F_01\wav/l_8820_9970_C1_F_01.wav'


(fs, audio) = wav.read(input_dir)



x, fs_1 = li.load(input_dir,sr=16000)



print("现在输出scipy读取的文件")
print(audio.shape)
print(audio)
print("现在输出librosa读取的文件")
print(x.shape)
print(x)
