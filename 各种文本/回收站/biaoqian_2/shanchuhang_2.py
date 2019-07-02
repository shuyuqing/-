# import glob
#删除メルフィルタバンク特征值文件中的前几行跟后面几行（被打上标签“9”的那几行特征值）
import os
def shanchuhang(lujin):

    # indir=r'C:\Users\a7825\Desktop\xinde_log_1'
    #保存处理之后的文件
    indir = lujin
    # list = glob.glob(indir+'/*.csv')  # 查看同文件夹下的csv文件数
    for i in os.listdir(indir):
    # for i in list:  # 循环读取同文件夹下的csv文件
        i = os.path.join(indir, i)
        d = open(i).readlines()
        # 删除第一行
        # for x in [0, 1, 2, 3, 4]:
        #     d[x] = ''
        # 删除第二行 d[1]=''
        # 删除倒数第一行 d[-1]=''
        # 删除倒数第二行 d[-2]=''
        jishu = 0#计数器，为了改变d的内容，作为下标使用，d就是一行一行的特征值
        for m in d:
            # print(m[0])
            # os.system("pause")
            if m[0] == '9':
                d[jishu] = ''#要想确实地改变d的内容，就只能通过一个计数器jishu来作为下标去改变d里面的内容

            jishu = jishu + 1

        # with open(outdir+'/'+i,'w') as f:
    #正好把原文件覆盖了
        with open(i, 'w') as f:
            f.writelines(d)

# if __name__ == '__main__':
#  shanchuhang(lujin)