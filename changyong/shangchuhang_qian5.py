# import glob
#删除一个文件中的前几行跟后面几行
#变种shanchuhang,先把文件复制到log里面，在log里面删除
import os
import muluzai as mulu
from shutil import copyfile

basedir = r'C:\Users\a7825\Desktop\工作空间\语音数据\UUDB\第一次实验\打标签\第五批'

def shanchuhang(baseindir):

    log = r'log_qian5'
    log_yuan = r'log_yuan'

    basedir = baseindir


    for mulu_1 in os.listdir(basedir):

        dir_1 = os.path.join(basedir,mulu_1,log)

        mulu.mkdir(dir_1)
        dir_2 = os.path.join(basedir,mulu_1,log_yuan)

        for u in os.listdir(dir_2):

            copyfile(os.path.join(dir_2, u), os.path.join(dir_1, u))  # 自动复制

        # list = glob.glob(indir+'/*.csv')  # 查看同文件夹下的csv文件数

    for neirong in os.listdir(basedir):
    # for i in list:  # 循环读取同文件夹下的csv文件
        neirong_1 = os.path.join(basedir, neirong,log)

        for i in os.listdir(neirong_1):

            i = os.path.join(neirong_1,i)

            d=open(i).readlines()
            # 删除第一行
            for x in [0, 1, 2, 3, 4]:
                 d[x] = ''
            # 删除第二行 d[1]=''
            # 删除倒数第一行 d[-1]=''
            # 删除倒数第二行 d[-2]=''
            # for m in [-1, -2, -3, -4, -5, -6]:
            #     d[m] = ''

            # with open(outdir+'/'+i,'w') as f:
        #正好把原文件覆盖了
            with open(i, 'w') as f:
                f.writelines(d)