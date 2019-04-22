import numpy as np
import os
from scipy.io import wavfile

path = r'C:\Users\a7825\Desktop\新建文件夹'
newpath = r'C:\Users\a7825\Desktop\新建文件夹 (4)'


for wave in os.listdir(path):
    path_1 = os.path.join(path,wave)
    sampleRate,musicData = wavfile.read(path_1)
    left = []
    right = []
    for item in musicData:
        left.append(item[0])
        right.append(item[1])
    wavfile.write(os.path.join(newpath,'left_'+wave), sampleRate, np.array(left))
    wavfile.write(os.path.join(newpath,'right_'+wave), sampleRate, np.array(right))