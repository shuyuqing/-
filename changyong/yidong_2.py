import os, os.path,shutil
import sys
import os, os.path,shutil
import sys
import muluzai as mulu
import chawenjian as cha

str_1 = ".out"
str_2 = ".wav"

path = r"C:\Users\a7825\Desktop\shiyan\ag1"#批次

for filename in os.listdir(path):
    path_2 = os.path.join(path,filename,'wav')#注意这里需要根据实际的目录改一下

    outlist = []
    wavlist = []

    for name in os.listdir(path_2):
        if str_1 in name:
            outlist.append(name.replace(str_1,''))

        elif str_2 in name:
            wavlist.append(name.replace(str_2,''))

    for name_2 in wavlist:
        if not name_2 in outlist:
            path_1 = os.path.join(path_2,name_2+str_2)
            os.remove(path_1)

for filename in os.listdir(path):
    path_1 = os.path.join(path,filename,'wav')#这里要根据实际的目录进行修改
    path_out = os.path.join(path,filename,'keka_yinsu')
    mulu.mkdir(path_out)

    for filename_1 in os.listdir(path_1):
        if filename_1.endswith(str_1):

            wenjian = os.path.join(path_1,filename_1)
            shutil.move(wenjian,path_out)

cha.chawenjianla(path)#找出不符合要求的.out文件，并把对应的.out文件跟.wav文件都删除掉