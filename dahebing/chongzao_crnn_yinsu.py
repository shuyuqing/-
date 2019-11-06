import os
import copy
# import pykakasi #把平假名或片假名转化为读音
# import make_kana_convertor
# import strQ2B


def chongzao(l_biaozhi, dianout_2, ID):#四个参数分别是标志list/scoring之后的识别结果/通过.out文件解析出来的list/文件ID

    jishuqi_dianout = 0

    dianout_3 = copy.deepcopy(dianout_2)#为了不改变函数外面的dianout的值


    # print(dianout_3)
    # print(l_biaozhi)
    # print(len(dianout_3))
    # print(len(l_biaozhi))
    # os.system('pause')

    for i in l_biaozhi:

        if i != 'D':

            try:

                dianout_3[jishuqi_dianout].append(i)

            except:

                print(ID)
                print('这个文件的标志个数跟转化(长母音)之后的单词的个数对不上')
                os.system('pause')

            jishuqi_dianout += 1

    return dianout_3

