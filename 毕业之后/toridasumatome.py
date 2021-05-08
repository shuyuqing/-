#把目录里面的文件全部都拿出来，统一放到一个文件夹下面

import os;
from shutil import copyfile

Path=r"C:\Users\a7825\Desktop\server"

def getAllFiles(path):
    flist = []
    for root, dirs, fs in os.walk(path):
        for f in fs:
            f_fullpath = os.path.join(root, f)
            # f_relativepath = f_fullpath[len(path):]#获取文件相对路径
            flist.append(f_fullpath)
    return flist

def matome(afiles):
    newfile=os.path.join(Path,"matome")
    os.makedirs(newfile)#创建文件夹
    for path in afiles:
        copyfile(path,os.path.join(newfile,os.path.basename(path)))#复制文件

if __name__ == '__main__':
    afiles = getAllFiles(Path)
    matome(afiles)
    print("\ndone!")