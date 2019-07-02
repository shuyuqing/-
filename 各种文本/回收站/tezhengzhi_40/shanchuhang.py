# import glob
#删除一个文件中的前几行跟后面几行
#变种shanchuhang,先把文件复制到log里面，在log里面删除
import os
import muluzai as mulu
from shutil import copyfile

def shanchuhang(path):

    basedir = path
    log = r'log'
    log_yuan = r'log_yuan'

    for mulu_1 in os.listdir(basedir):

        dir_1 = os.path.join(basedir,mulu_1,log)

        mulu.mkdir(dir_1)
        dir_2 = os.path.join(basedir,mulu_1,log_yuan)

        for u in os.listdir(dir_2):
            copyfile(os.path.join(dir_2, u), os.path.join(dir_1, u))  # 自动复制

        indir=dir_1
        #保存处理之后的文件

        # list = glob.glob(indir+'/*.csv')  # 查看同文件夹下的csv文件数
        for i in os.listdir(indir):
        # for i in list:  # 循环读取同文件夹下的csv文件
            i = os.path.join(indir, i)
            d=open(i).readlines()
            # 删除第一行
            for x in [0, 1, 2, 3, 4]:
                 d[x] = ''
            # 删除第二行 d[1]=''
            # 删除倒数第一行 d[-1]=''
            # 删除倒数第二行 d[-2]=''
            for m in [-1, -2, -3, -4, -5, -6]:
                d[m] = ''

            # with open(outdir+'/'+i,'w') as f:
        #正好把原文件覆盖了
            with open(i, 'w') as f:
                f.writelines(d)