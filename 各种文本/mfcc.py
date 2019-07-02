import scipy.io.wavfile as wav
from python_speech_features import mfcc
import numpy as np


fs, audio = wav.read(r"C:\Users\a7825\Desktop\工作空间\跑代码\python实验\读取音频文件/a01.wav")
feature_mfcc = mfcc(audio, samplerate=fs)
print(feature_mfcc.shape)
np.savetxt('new.csv', feature_mfcc, delimiter = ',')