#在把文件放入chasen之前，先把正解文的.txt文件整理出来
import csv,sys
#原来csv这个包是可以处理txt文件的
import os

pici = r"C:\Users\a7825\Desktop\工作空间\语音数据\UUDB\第一次实验\打标签\第五批"
#批次的目录

for ru in os.listdir(pici):

    wenjian = ru
    #属于哪个文件

    wenjian_1 = wenjian[0:4] + r'.txt'
    #生成的那个可以输入到chasen中去的文本文件

    # print(wenjian)
    # print(wenjian_1)
    # os.system('pause')

    #正解文的文件名，要从正解文中选出需要的正解文,注意，这个正解文里面每一行都必须有内容，每一行都不能为空
    #运行之后会生成一个文件名为'wenjian_1'+L的文件，这个文件就是要放入到chasen里的文件
    #之后，把这个文件放入到chasen中，手动复制粘贴chasen的出力结果，在跟wenjian_1文件相同目录之下创建一个名叫
    #'chasen.txt'的文件，然后把chasen的出力复制粘贴到这个文件中，之后用quci.py这个文本继续操作

    path = os.path.join(pici,wenjian,'keka')#正解文的目录
    pici_1 = os.path.join(pici,wenjian,wenjian_1)
    zhengjie = os.path.join(pici,wenjian,wenjian)+'.txt'#存放正解文的目录
    newlist = []

    txtwenjian = csv.reader(open(pici_1, 'r', encoding='utf-8'))
    b = [i for i in txtwenjian]
    # print(b)
    # os.system('pause')
    zhongzhuan = []

    with open(zhengjie,'w',encoding='utf-8') as f:  # 把正解文一句一句地写入新的txt文件
        for name in os.listdir(path):
            a = name[6:9]
            # print(a)
            # os.system('pause')
            zhengjie = b[int(a) - 1]
            #此时的zhengjie是一个list

            try:
                zhuanghuan = list(zhengjie[0])

            except:
                print('文件%s出了问题'%wenjian_1)
                os.system('pause')


            zhuanghuan.extend('。')#给每一句话的最后都加上一个句号
            zhuanghuan = ''.join(zhuanghuan)

            f.writelines(zhuanghuan + '\n')