# import glob
#删除一个文件中的前几行
#然后在矩阵后面补零
#生成的数据全部放入bulin中去，等着被很有苏北裤头日
import os
import numpy as np
import muluzai as mulu
from shutil import copyfile

baseindir=r'C:\Users\a7825\Desktop\工作空间\セミナー\语音'

bulin = 'bulin'
#保存处理之后的文件

log_yuan = 'log_qian5'

indir = os.path.join(baseindir,bulin)
#删除了前几行并补了零的fbank的地址

indir_fuzhi = os.path.join(baseindir,log_yuan)
#抽取出来什么也没有删除过的fbank的地址

def shanchuhang():

    # list = glob.glob(indir+'/*.csv')  # 查看同文件夹下的csv文件数
    # for i in os.listdir(indir):
    # # for i in list:  # 循环读取同文件夹下的csv文件
    #     i = os.path.join(indir, i)
    #     d=open(i).readlines()
    #     # 删除第一行
    #     for x in [0, 1, 2, 3, 4]:
    #          d[x] = ''
    #     # 删除第二行 d[1]=''
    #     # 删除倒数第一行 d[-1]=''
    #     # 删除倒数第二行 d[-2]=''
    #     # for m in [-1, -2, -3, -4, -5, -6]:
    #     #     d[m] = ''
    #     # with open(outdir+'/'+i,'w') as f:
    # #正好把原文件覆盖了
    #     with open(i, 'w') as f:
    #         f.writelines(d)

    for i in os.listdir(indir):
        a = np.loadtxt(os.path.join(indir, i), delimiter=',', skiprows=0).astype(np.float32)
        lin = np.zeros((25,np.shape(a)[1]))#注意这里的行数等于block减去一再减去6
        c = np.vstack((a,lin))

        np.savetxt(os.path.join(indir, i), c,delimiter=',')


if __name__ == '__main__':

    mulu.mkdir(indir)

    for u in os.listdir(indir_fuzhi):
        copyfile(os.path.join(indir_fuzhi,u),os.path.join(indir,u))#自动复制

    shanchuhang()