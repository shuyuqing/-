import scipy.io.wavfile as wav
from python_speech_features.base import mfcc,fbank,logfbank
import numpy as np
import os

input_dir = r"C:\Users\a7825\Desktop\工作空间\跑代码\打标签\F1\B\wav_16"
output_dir1 = r"C:\Users\a7825\Desktop\工作空间\跑代码\打标签\F1\B\melbank"
output_dir2 = r"C:\Users\a7825\Desktop\工作空间\跑代码\打标签\F1\B\log"
if __name__ == "__main__":

    for ad_file in os.listdir(input_dir):
        (fs, audio) = wav.read(input_dir + "/" + ad_file)
        feature_m, feature_n = fbank(audio, fs, winfunc=np.hamming)
        log = logfbank(audio,fs)
        np.savetxt(output_dir1 + "/" + ad_file + ".fbank.csv", feature_m, delimiter=',')
        np.savetxt(output_dir2 + "/" + ad_file + ".log.csv", log, delimiter=',')
        # 拼接字符串，把单引号改成双引号居然好使


# fs, audio = wav.read(r"C:\Users\a7825\Desktop\新しいフォルダー/a.wav")
# # feature_mfcc = mfcc(audio, samplerate=fs, numcep=40, nfilt=40)
# feature_m,feature_n = fbank(audio, fs)
# feature_log = logfbank(audio, fs)
# # print(feature_mel[0].shape)
# # print(feature_m)
# # print(feature_n.shape)
# np.savetxt('fbank.csv', feature_m, delimiter = ',')
# np.savetxt('energy.csv', feature_n, delimiter= ',')
# # np.savetxt('log.csv', feature_log, delimiter =',')
#
# # print(fs)
# # print(feature_mfcc.shape)
