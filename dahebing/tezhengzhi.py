#提取各种特征值
import scipy.io.wavfile as wav
from python_speech_features.base import mfcc,fbank,logfbank
import numpy as np
import os
import muluzai as muluz


def tiqu(path,weidu,logenergy,energy_1):

    basedir = path
    for mulu in os.listdir(basedir):

        input_dir = os.path.join(basedir,mulu,"wav")
        #语音文件的路劲

        output_dir2 = os.path.join(basedir,mulu,'log_yuan')
        #log梅尔普系数


        # output_dir3 =r"C:\Users\a7825\Desktop\工作空间\语音数据\UUDB\第一次实验\打标签\第三批\C063L\mfcc"
        #mfcc

        muluz.mkdir(output_dir2)

        for ad_file in os.listdir(input_dir):
            (fs, audio) = wav.read(input_dir + "/" + ad_file)

            if energy_1 == True:
                feat, energy = fbank(audio, fs, nfilt=weidu)
                np.savetxt(output_dir2 + "/" + ad_file + ".csv", feat, delimiter=',')

            if logenergy == True:
                log = logfbank(audio, fs, nfilt=weidu)
                np.savetxt(output_dir2 + "/" + ad_file + ".csv", log, delimiter=',')


            # print(feat)
            # log = logfbank(audio,fs,nfilt=weidu)
            # mf = mfcc(audio)

            # np.savetxt(output_dir2 + "/" + ad_file + ".csv", log, delimiter=',')
            # np.savetxt(output_dir3 + "/" + ad_file + ".csv", mf, delimiter=',')
            # 拼接字符串，把单引号改成双引号居然好使
