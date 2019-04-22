import os, os.path,shutil
import sys
import os, os.path,shutil
import sys
import muluzai as mulu

str_1 = ".out"
str_2 = ".wav"

path = r"C:\Users\a7825\Desktop\工作空间\语音数据\RWCP-SP96-要切\第一批 - 副本 (2)\特别处理"#批次

for filename in os.listdir(path):
    path_2 = os.path.join(path, filename, 'wav')  # 以wav文件夹下的文件为基准，删除keka文件夹下的文件
    path_3 = os.path.join(path, filename, 'keka')

    outlist = []
    wavlist = []

    for name in os.listdir(path_2):
        wavlist.append(name.replace(str_2,''))

    for filename_1 in os.listdir(path_3):
        filename_1_1 = filename_1.replace(str_1,'')
        if not filename_1_1 in wavlist:
            path_shan = os.path.join(path_3,filename_1)
            os.remove(path_shan)