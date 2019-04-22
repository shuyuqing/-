import os
import scipy.io.wavfile as wav
from python_speech_features import mfcc
import numpy as np

input_dir = r"C:\Users\a7825\Desktop\工作空间\语音数据\ogvc_16\M2\A\wav_16"
output_dir = r"C:\Users\a7825\Desktop\工作空间\语音数据\ogvc_16\M2\A\mfcc_13"
if __name__ == "__main__":

 for ad_file in os.listdir(input_dir):
     fs, audio = wav.read(input_dir+"/"+ad_file)
     feature_mfcc = mfcc(audio, samplerate=fs)
     print(feature_mfcc.shape)
     np.savetxt(output_dir+"/"+ad_file+".csv", feature_mfcc, delimiter = ',')
     #拼接字符串，把单引号改成双引号居然好使