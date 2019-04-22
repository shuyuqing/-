# import glob
#删除一个文件中的前几行跟后面几行
import os

def shanchuhang():


    indir=r'C:\Users\a7825\Desktop\工作空间\语音数据\UUDB\第一次实验\打标签\log\新建文件夹'
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

if __name__ == '__main__':
 shanchuhang()