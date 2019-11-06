# import glob
#删除一个文件中的前几行
#然后在矩阵后面补零
#生成的数据全部放入bulin中去，等着被很有苏北裤头日
import os
import numpy as np
from shutil import copyfile
def hencyou_1(path,chuangkou,padding,lintianchong):

    baseindir = path
    shanchuhang(baseindir)#删除前五行
    mizhichuli(baseindir,chuangkou,padding,lintianchong)#进行変調スペクトル的计算


# import glob
#删除一个文件中的前几行
#先把文件复制到log里面，在log里面删除
import os
from shutil import copyfile

def shanchuhang(baseindir):

    log = r'log_qian5'
    log_yuan = r'log_yuan'
    basedir = baseindir

    for mulu_1 in os.listdir(basedir):
        dir_1 = os.path.join(basedir,mulu_1,log)
        mkdir(dir_1)
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
            for x in [0, 1, 2, 3, 4]:#前五行被删除了
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

import os

def mkdir(path):#没有就创建目录

    # 去除首位空格
    # path = path.strip()
    # 去除尾部 \ 符号
    # path = path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print(path + ' 创建成功')
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')

# # 定义要创建的目录
# mkpath = "d:\\qttc\\web\\"
# # 调用函数
# mkdir(mkpath)



# 把从语音文件中提取特征值转变成很雀死白裤托落
import numpy as np
import numpy.fft as nf
import scipy.fftpack as sc
# numpy跟scipy都提供了fft这个函数
import os,math
import math as ma

def mizhichuli(basedir,chuangkou,padding,lintianchong):

    jiachuang = True
    bulin = 'log_qian5'
    mizhichuli_log = 'mizhichuli'

    for mulu_1 in os.listdir(basedir):#每次循环可以处理一个大文件，如‘C1_F_05’
        lujing = os.path.join(basedir, mulu_1, mizhichuli_log)
        # 处理之后的特征值文件应该存放的地方
        filepath = os.path.join(basedir, mulu_1, bulin)
        # 需要被处理的特征值文件
        mkdir(lujing)
        xuhao = 1

        for name in os.listdir(filepath):#每个循环能够处理一个文件

            start = 0
            file_path = os.path.join(filepath, name)
            final_path = os.path.join(lujing, str(xuhao) + '_' + name)
            tezheng = np.loadtxt(file_path, delimiter=',')
            cishu = tezheng.shape[0] - chuangkou +1 #在进行傅里叶变化的时候每个窗口需要沿时间轴挪动的次数
            tezheng = np.array(tezheng, float)
            tezheng = np.transpose(tezheng)
            global block, start, end, huishu

            if lintianchong == True:  # 如果要进行零填充，这个变量就要设置为True
                # print(zhenggui_list_1)
                # os.system('pause')
                lin = np.zeros(padding)  # 进行零补充

            jieguo = []
            for yihang in tezheng:#每一个循环进行一个bin的变换

                xinhao_1 = yihang[start:start+chuangkou]
                # print(xinhao_1)
                # os.system('pause')
                xinhao_1 = np.hstack((xinhao_1,lin))
                xinhao_1 = jiachuangzi(xinhao_1)  # 加窗
                xinhao_1 = nf.fft(xinhao_1)
                # print(xinhao_1)
                xinhao_1 = abs(xinhao_1)
                # print(xinhao_1)
                # print(xinhao_1.shape)
                xinhao_1 = xinhao_1[:int((xinhao_1.shape[0])/2)]
                xinhao_1 = xinhao_1.tolist()
                jieguo.append(xinhao_1)

            print(jieguo)
            jieguo = np.array(jieguo)
            jieguo = np.transpose(jieguo)
            np.savetxt(final_path, jieguo, delimiter=',')
            xuhao += 1

            print(jieguo)
            print(jieguo.shape)
            os.system('pause')
                # print(xinhao_1)
                # print(xinhao_1.shape)
                # os.system('pause')

            hang = tezheng.shape[0]
            lie = tezheng.shape[1]
            # 获得特征值矩阵的行数和列数
            newtezheng = []

            block = chuangkou
            # block是窗口的大小
            huishu = hang - block + 1
            # 每一列要做的傅里叶变化的次数
            end = block
            tezheng_3 = [[] for row in range(huishu)]
            # print(len(tezheng_3))

            for i in range(lie):
                # print("现在处理第%d列"%i)
                start = 0
                end = block
                tezheng_1 = np.loadtxt(file_path, delimiter=',', usecols=(i))
                # 一列一列第取出数据，usecols起到了这个作用
                N = block
                for m in range(huishu):#m是tezheng_3这个列表里面的序号
                    zhenggui_list_1 = []
                    for u in tezheng_1[start:end]:
                        zhenggui_list_1.append(u)
                    zhenggui_list_1 = np.array(zhenggui_list_1)
                    if jiachuang == True:
                        zhenggui_list_1 = jiachuangzi(zhenggui_list_1)#加窗
                    if lintianchong == True:#如果要进行零填充，这个变量就要设置为True
                        # print(zhenggui_list_1)
                        # os.system('pause')
                        lin = np.zeros(padding)#进行零补充
                        zhenggui_list_1 = np.hstack((zhenggui_list_1, lin))
                        # print(zhenggui_list_1)
                        # os.system('pause')
                    tezheng_2 = nf.fft(zhenggui_list_1)
                    # print(tezheng_2)
                    # print("第%d列的第%d波"%(i,m))
                    # print(tezheng_2)
                    block_1 = block + padding
                    # print('输出block')
                    # print(block_1)
                    q = int(block_1 / 2)
                    # for n in range(q, block_1):  # 之前括号里面的值是block_1,因为要扔掉一半所以改了
                    zhongzhuan = []

                    for n in range(0, q):  # 要取前半部分
                        zhongzhuan.append(ma.sqrt(ma.pow(tezheng_2[n].imag, 2) + ma.pow(tezheng_2[n].real, 2)))
                    zhongzhuan = np.array(zhongzhuan)
                    zhongzhuan = zhenggui(zhongzhuan,int(zhongzhuan.shape[0]))#正规化的部分
                    tezheng_3[m].extend(zhongzhuan)
                    # print(tezheng_3)
                    # os.system('pause')
                    # tezheng_3[m] = np.array(tezheng_3[m])
                    # tezheng_3[m] = zg.zhenggui(tezheng_3[m],int(tezheng_3[m].shape[0]))
                    start = start + 1
                    end = end + 1
            newtezheng = np.array(tezheng_3, dtype=np.float)
            # newtezheng = np.transpose(newtezheng)
            np.savetxt(final_path, newtezheng, delimiter=',')

import numpy as np
def jiachuangzi(a):#进行加窗处理

    a = np.array(a,float)
    window = np.hamming(len(a))
    n=0

    for i in window:
        a[n] = a[n]*i
        n = n+1
    return a


import math,os
import numpy as np

def zhenggui(zhenggui_4,block):#进行正规化处理

    zhenggui_list_1 = []
    pingfanghe = 0
    N = block
    for d in zhenggui_4:
        pingfanghe += math.pow(d, 2)
    xishu = math.sqrt(N / pingfanghe)

    for u in zhenggui_4:
        zhenggui_list_1.append(u * xishu)
    zhenggui_list_1 = np.array(zhenggui_list_1)
    return zhenggui_list_1


