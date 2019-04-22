# import glob
#删除一个文件中的前几行
#然后在矩阵后面补零
#生成的数据全部放入bulin中去，等着被很有苏北裤头日
import os
import numpy as np
import muluzai as mulu
from shutil import copyfile
import shangchuhang_qian5 as shanchu
import fuliye_gai as fu

def hencyou_1(path):

    baseindir = path
    shanchu.shanchuhang(baseindir)#删除前五行和后六行

    for mulu_1 in os.listdir(baseindir):

        bulin = 'bulin'
        #保存处理之后的文件

        log_yuan = 'log_qian5'

        indir = os.path.join(baseindir,mulu_1,bulin)
        #删除了前几行并补了零的fbank的地址

        indir_fuzhi = os.path.join(baseindir,mulu_1,log_yuan)
        #抽取出来什么也没有删除过的fbank的地址

        mulu.mkdir(indir)

        for u in os.listdir(indir_fuzhi):
            copyfile(os.path.join(indir_fuzhi,u),os.path.join(indir,u))#自动复制

        for i in os.listdir(indir):
            a = np.loadtxt(os.path.join(indir, i), delimiter=',', skiprows=0).astype(np.float32)
            lin = np.zeros((63,np.shape(a)[1]))#注意这里的行数等于block减去一，而且给矩阵补了零
            c = np.vstack((a,lin))

            np.savetxt(os.path.join(indir, i), c,delimiter=',')

    fu.mizhichuli(baseindir)#进行変調スペクトル的计算