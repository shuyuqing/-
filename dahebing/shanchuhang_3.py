# import glob
#删除メルフィルタバンク特征值文件中的前几行跟后面几行（被打上标签“9”的那几行特征值）
import numpy as np
import os
def shanchuhang(lujin):

    # indir=r'C:\Users\a7825\Desktop\xinde_log_1'
    #保存处理之后的文件
    indir = lujin
    # list = glob.glob(indir+'/*.csv')  # 查看同文件夹下的csv文件数
    for i in os.listdir(indir):
    # for i in list:  # 循环读取同文件夹下的csv文件
        i = os.path.join(indir, i)
        tezheng_1 = np.loadtxt(i, delimiter=',', usecols=(0))

        print(tezheng_1)
        os.system('pasue')

        d_1 = open(i)
        d = d_1.readlines()
        # 删除第一行
        # for x in [0, 1, 2, 3, 4]:
        #     d[x] = ''
        # 删除第二行 d[1]=''
        # 删除倒数第一行 d[-1]=''
        # 删除倒数第二行 d[-2]=''
        jishu = 0#计数器，为了改变d的内容，作为下标使用，d就是一行一行的特征值
        # print(len(d))
        # os.system('pause')
        # print(d[0][0])
        # print(d[1][0])
        # print(d[2][0])
        for m in tezheng_1:
            # print(m)
            # print(len(m))
            # os.system("pause")
            if int(m)!=0 and int(m)!=1:#
                print(i)
                print(m)
                # os.system('pause')
                d[jishu] = ''#要想确实地改变d的内容，就只能通过一个计数器jishu来作为下标去改变d里面的内容

            jishu = jishu + 1

        d_1.close()

        # with open(outdir+'/'+i,'w') as f:
    #正好把原文件覆盖了
        with open(i, 'w') as f:
            f.writelines(d)

shanchuhang(lujin=r'C:\Users\a7825\Desktop\新しいフォルダー\kyo0211l\mizhichuli_biaoqian')