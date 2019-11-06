#用CCSCC那种记号来照合正解文
import re,os,csv
import pipei_yinsu as pi
import muluzai as mulu
import chongzao_crnn_yinsu as cz
from quci_RWCP_SP96_yinsu import changpoyin

#为了处理那些因为表示方式不同而被打错标签的单词，先把错误单词的索引找出，再把单词转变成字母，然后再比较

def dabiaoqian(path,guanjianzi_1,guanjianzi_2):

    name_tezheng = guanjianzi_1
    # 装有特征值的那个文件的文件名

    xinde = guanjianzi_2
    # 装入新的特征值的文件名

    name1 = 'align1'
    name2 = 'symbol.txt'
    #标志文件的名字，当align1不好使的时候，换用symbol.txt,注意，下面的代码相应地也要换掉

    for i in os.listdir(path):

        path_1 = os.path.join(path,i)

        path_out = os.path.join(path_1,'keka_yinsu')

        path_tezheng = os.path.join(path_1, name_tezheng)

        print(os.path.join(path_1, name1))

        biaozhiwenjian = csv.reader(open(os.path.join(path_1, name1), 'r', encoding='EUC-JP'))  # 出现错误时候可能是没加encoding
        # biaozhiwenjian = csv.reader(open(os.path.join(path_1, name1), 'r'))  # 把标志文件读进来

        # biaozhiwenjian = csv.reader(open(os.path.join(path_1, name2), 'r', encoding='utf-8')) #如果标志文件是.txt文件
        biaozhiwenjian_1 = [i for i in biaozhiwenjian]  # 转化为list,但是内容是list里面套list
        #[['id: l_8840_9810_T1_F_01'],['REF:  そう です か 、 はい 。 '],['HYP:  そう です か    はい 。 '],['EVAL: C    C    C  D  C    C  '],[],['id: l_10800_13190_T1_F_01']]

        path_xinde = os.path.join(path_1, xinde)
        mulu.mkdir(path_xinde)

        for i in range(0, len(biaozhiwenjian_1)):  # 这里的每一轮可以为一个语音文件打标签

            try:
                biaozhi = biaozhiwenjian_1[i][0]

            except:

                continue

            if 'id:' in biaozhi:

                ID = biaozhiwenjian_1[i][0].replace('id: ', '')

                l_zhengjie = biaozhiwenjian_1[i + 1][0].split()#取REF
                l_zhengjie.pop(0)

                l_jieguo = biaozhiwenjian_1[i + 2][0].split()#取HYP
                l_jieguo.pop(0)

                l_biaozhi = biaozhiwenjian_1[i + 3][0].split()#取EVAL
                l_biaozhi.pop(0)

                #建立严格对应的正解，识别结果，标记，如果标记是d的话，结果就是空
                jishuqi_jieguo = 0
                jishuqi_zhengjie = 0
                jishuqi_biaozhi = 0

                for i in l_biaozhi:

                    if i == "D":#删除错误
                        jishuqi_zhengjie += 1
                        jishuqi_biaozhi += 1

                    if i == "C":#正解
                        jishuqi_zhengjie += 1
                        jishuqi_jieguo += 1
                        jishuqi_biaozhi += 1

                    if i == "I":#插入错误
                        jishuqi_jieguo += 1
                        jishuqi_biaozhi += 1

                    if i == "S":#如果是S的话特殊处理一下，转化为字母再比较，如果转化之后相等的话，把标志改为C

                        jishuqi_zhengjie += 1
                        jishuqi_jieguo += 1
                        jishuqi_biaozhi += 1

                path_out_1 = os.path.join(path_out, ID + '.out')#读出.out文件
                dianout = pi.read_out(path_out_1)
                # start = dianout.pop(0)[1][1]  # 给开始的无音区间打标签9，pop掉第一个元素
                start = dianout[0][1][0] - 1
                # start_1 = dianout[-1][1][0]#给末尾句号打标签9
                start_1 = dianout[-1][1][1]+1
                # end_1 = dianout.pop(-1)[1][1] 因为在提取特征值的时候最后一帧可能被丢了，所以这个end就用t_file_list的条数代替
                # print(dianout)
                # os.system('pause')
                # 最后的效果:[['', [0, 18]], ['お', [19, 24]], ['願い', [25, 49]], ['三', [50, 82]], ['。', [83, 86]]]

                path_tezheng_1 = os.path.join(path_tezheng, ID + '.wav.csv')
                tezhengzhi = csv.reader(open(path_tezheng_1, 'r', encoding='utf-8'))
                t_file_list = [i for i in tezhengzhi]

                end_1 = len(t_file_list)-1

                if start< len(t_file_list):#如果.out文件的空白部分的帧数范围大于特征值的行数，就扔了

                    for i in range(start + 1):
                        t_file_list[i].insert(0, '9')  #最前面的无音区间全部都打标签9,把它们当做正确认识来处理

                    for i in range(start_1, end_1 + 1):
                        t_file_list[i].insert(0, '9')

                    # l_jieguo_1.pop(-1)#最后句号的部分已经打过标签了，需要把它pop掉

                    print("ID")
                    print(ID)


                    _dianout = changpoyin(dianout,path_out_1,ID + '.out')#把有长母音的地方处理一下

                    dianout_chongzao = cz.chongzao(l_biaozhi, _dianout, ID)  #生成新的dianoutlist,以后就靠它了

                    # print('dianout_chongzao')
                    # print(dianout_chongzao)
                    #通过得到的新的list,开始打标签
                    # [['災害', [3, 40], 'C'], ['で', [41, 48], 'C'], ['ござい', [49, 77], 'C'], ['ます', [78, 98], 'C'],['から', [99, 130], 'C'], ['、', [131, 152], 'C'], ['その', [153, 177], 'C'], ['場', [178, 190], 'C'],['で', [191, 209], 'C']]
                    for i in dianout_chongzao:
                        start, end = i[1]
                        if start <= end_1:
                            if end_1 <= end:
                                end = end_1
                            if i[2] == 'C':
                                for b in range(start, end+1):
                                    t_file_list[b].insert(0, '0')
                            else:

                                for b in range(start, end+1):
                                    t_file_list[b].insert(0, '1')

                    changdu = len(t_file_list[0])#为了给逗号的部分打标签做准备，逗号在取得.out文件之前就已经被删掉了

                    n = 0
                    for item in t_file_list:#给逗号的部分打标签
                        if len(item)!=changdu:
                            t_file_list[n].insert(0, '0')
                        n = n + 1

                    path_xinde_tezhengzhi = os.path.join(path_xinde, ID + '.csv')

                    with open(path_xinde_tezhengzhi, 'w+', encoding='utf-8') as mergen_file:
                        for i in t_file_list:
                            mergen_file.write('%s\n' % ','.join(i))

        shanchuhang(path_xinde)  # 把有标记9的特征值全部都删除掉


# import glob
#删除メルフィルタバンク特征值文件中的前几行跟后面几行（被打上标签“9”的那几行特征值）
import numpy as np
import os
def shanchuhang(lujin):

    indir = lujin
    for i in os.listdir(indir):
        i = os.path.join(indir, i)
        tezheng_1 = np.loadtxt(i, delimiter=',', usecols=(0))
        d_1 = open(i)
        d = d_1.readlines()#只能把数字识别成字符串，无法读取数字
        # 删除第一行
        # for x in [0, 1, 2, 3, 4]:
        #     d[x] = ''
        # 删除第二行 d[1]=''
        # 删除倒数第一行 d[-1]=''
        # 删除倒数第二行 d[-2]=''
        jishu = 0#计数器，为了改变d的内容，作为下标使用，d就是一行一行的特征值
        for m in tezheng_1:
            if int(m)!=0 and int(m)!=1:#
                d[jishu] = ''#要想确实地改变d的内容，就只能通过一个计数器jishu来作为下标去改变d里面的内容
            jishu = jishu + 1
        d_1.close()
        with open(i, 'w') as f:
            f.writelines(d)

# dabiaoqian(path=r'C:\Users\a7825\Desktop\新建文件夹\新建文件夹',guanjianzi_1=r'mizhichuli',guanjianzi_2=r'mizhichuli_biaoqian_shiyan')
