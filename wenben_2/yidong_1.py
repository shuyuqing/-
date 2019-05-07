import os, os.path,shutil
import sys
import muluzai as mulu

str = ".out"

path = r"C:\Users\a7825\Desktop\shiyan\symbol"#批次


for filename in os.listdir(path):
    path_1 = os.path.join(path,filename,'wav')#这里要根据实际的目录进行修改
    path_out = os.path.join(path,filename,'keka_yinsu')
    mulu.mkdir(path_out)

    for filename_1 in os.listdir(path_1):
        if filename_1.endswith(str):

            wenjian = os.path.join(path_1,filename_1)
            shutil.move(wenjian,path_out)

