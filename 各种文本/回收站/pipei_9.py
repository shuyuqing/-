#用CCSCC那种记号来照合正解文
import re,os,csv
import pipei as pi
from pykakasi import kakasi#把平假名或片假名转化为读音
import muluzai as mulu
import shanchuhang_2 as shanchu#为了除去那些被打上标签9的特征值
import strQ2B
import make_kana_convertor
import chongzao_1 as cz

#打标签的思路是：因为CCSS的符号是跟正解文,识别结果两个中比较长的一个对应的，这个是最大的难点，所以要做的是先去找标志文件里面的C,
#也就是正确认识的单词，然后返回这些C的索引，然后根据索引去识别结果(正解文)中找被正确识别的单词，注意只有识别结果才对应帧数表，找到之后把单词顺序插入到一个list中去，
#在用识别结果里的单词去对应这个list,按顺序一个单词一个单词地对，每成功对应上一个单词就从list中把这个单词删除掉，并获取这个单词
#的帧数表，然后打上标签0，没有对应上的单词就在这个单词的范围内打上标签1
#为了处理那些因为表示方式不同而被打错标签的单词，先把错误单词的索引找出，再把单词转变成字母，然后再比较

def dabiaoqian(path):

    from pykakasi import kakasi
    import csv, os

    name_tezheng = 'mizhichuli_log'
    # 装有特征值的那个文件的文件名

    xinde = 'xinde_mizhichuli'
    # 装入新的特征值的文件名

    name1 = 'align1'
    name2 = 'symbol.txt'
    #标志文件的名字，当align1不好使的时候，换用symbol.txt,注意，下面的代码相应地也要换掉

    kakasi = kakasi()
    kakasi.setMode("H", "a")  # Hiragana to ascii, default: no conversion
    kakasi.setMode("K", "a")  # Katakana to ascii, default: no conversion
    kakasi.setMode("J", "a")  # Japanese to ascii, default: no conversion
    kakasi.setMode("r", "Hepburn")  # default: use Hepburn Roman table
    kakasi.setMode("s", True)  # add space, default: no separator
    conv = kakasi.getConverter()

    for i in os.listdir(path):

        path_1 = os.path.join(path,i)

        path_out = os.path.join(path_1,'keka')

        path_tezheng = os.path.join(path_1, name_tezheng)

        #biaozhiwenjian = csv.reader(open(os.path.join(path_1, name1), 'r', encoding='EUC-JP'))  # 把标志文件读进来
        biaozhiwenjian = csv.reader(open(os.path.join(path_1, name2), 'r', encoding='utf-8')) #如果标志文件是.txt文件

        biaozhiwenjian_1 = [i for i in biaozhiwenjian]  # 转化为list,但是内容是list里面套list
        #[['id: l_8840_9810_T1_F_01'],['REF:  そう です か 、 はい 。 '],['HYP:  そう です か    はい 。 '],['EVAL: C    C    C  D  C    C  '],[],['id: l_10800_13190_T1_F_01']]

        # print(biaozhiwenjian_1)
        # os.system('pause')

        path_xinde = os.path.join(path_1, xinde)
        mulu.mkdir(path_xinde)

        for i in range(0, len(biaozhiwenjian_1)):  # 这里的每一轮可以为一个语音文件打标签

            try:
                biaozhi = biaozhiwenjian_1[i][0]

            except:

                continue

            if 'id:' in biaozhi:

                ID = ''
                l_biaozhi = []
                l_zhengjie = []
                l_zhengjie_1 = []
                l_jieguo = []
                l_jieguo_1 = []

                ID = biaozhiwenjian_1[i][0].replace('id: ', '')

                l_zhengjie = biaozhiwenjian_1[i + 1][0].split()
                l_zhengjie.pop(0)

                l_jieguo = biaozhiwenjian_1[i + 2][0].split()
                l_jieguo.pop(0)

                l_biaozhi = biaozhiwenjian_1[i + 3][0].split()
                l_biaozhi.pop(0)

                #建立严格对应的正解，识别结果，标记，如果标记是d的话，结果就是空
                jishuqi_jieguo = 0
                jishuqi_zhengjie = 0
                jishuqi_biaozhi = 0

                for i in l_biaozhi:

                    if i == "D":
                        l_zhengjie_1.append(l_zhengjie[jishuqi_zhengjie])
                        l_jieguo_1.append('')
                        jishuqi_zhengjie += 1
                        jishuqi_biaozhi += 1

                    if i == "C":
                        l_zhengjie_1.append(l_zhengjie[jishuqi_zhengjie])
                        l_jieguo_1.append(l_jieguo[jishuqi_jieguo])
                        jishuqi_zhengjie += 1
                        jishuqi_jieguo += 1
                        jishuqi_biaozhi += 1

                    if i == "I":
                        l_jieguo_1.append(l_jieguo[jishuqi_jieguo])
                        l_zhengjie_1.append('')
                        jishuqi_jieguo += 1
                        jishuqi_biaozhi += 1

                    if i == "S":#如果是S的话特殊处理一下，转化为字母再比较，如果转化之后相等的话，把标志改为C
                        l_zhengjie_1.append(l_zhengjie[jishuqi_zhengjie])
                        l_jieguo_1.append(l_jieguo[jishuqi_jieguo])

                        zhengjie_hanzi = l_zhengjie[jishuqi_zhengjie]
                        jieguo_hanzi = l_jieguo[jishuqi_jieguo]

                        #先处理识别结果
                        if conv.do(jieguo_hanzi) == jieguo_hanzi and jieguo_hanzi != '、':#判断是不是字母

                            try:
                                zhuanhuan_jieguo = conv.do(make_kana_convertor._make_kana_convertor(strQ2B.strQ2B(jieguo_hanzi)))

                            except:
                                zhuanhuan_jieguo = conv.do(make_kana_convertor._make_kana_convertor(jieguo_hanzi))

                        else:
                            zhuanhuan_jieguo = conv.do(jieguo_hanzi)

                        #再处理正解文
                        if conv.do(zhengjie_hanzi) == zhengjie_hanzi and zhengjie_hanzi != '、':  # 判断是不是字母

                            try:
                                zhuanhuan_zhengjie = conv.do(make_kana_convertor._make_kana_convertor(strQ2B.strQ2B(zhengjie_hanzi)))

                            except:
                                zhuanhuan_zhengjie = conv.do(make_kana_convertor._make_kana_convertor(zhengjie_hanzi))

                        else:
                            zhuanhuan_zhengjie = conv.do(zhengjie_hanzi)

                        if zhuanhuan_jieguo == zhuanhuan_zhengjie:

                            # print("正解list")
                            # print(l_zhengjie_1)
                            #
                            # print("识别结果list")
                            # print(l_jieguo_1)
                            #
                            # print("zhuanhuan_jieguo")
                            # print(zhuanhuan_jieguo)
                            # print("zhuanhuan_zhengjie")
                            # print(zhuanhuan_zhengjie)
                            # print("有标志被改了")
                            # print(ID)
                            # os.system("pause")

                            l_biaozhi[jishuqi_biaozhi] = 'C'

                        jishuqi_biaozhi += 1
                        jishuqi_zhengjie += 1
                        jishuqi_jieguo += 1

                # print(l_jieguo_1)
                # print(l_zhengjie_1)
                # print(l_biaozhi)
                # os.system('pause')

                path_out_1 = os.path.join(path_out, ID + '.out')#读出.out文件
                dianout = pi.read_out(path_out_1)
                start = dianout.pop(0)[1][1]  # 给开始的无音区间打标签9，pop掉第一个元素
                start_1 = dianout[-1][1][0]#给末尾句号打标签9
                # end_1 = dianout.pop(-1)[1][1]

                # print(dianout)
                # os.system('pause')
                # 最后的效果:[['', [0, 18]], ['お', [19, 24]], ['願い', [25, 49]], ['三', [50, 82]], ['。', [83, 86]]]

                path_tezheng_1 = os.path.join(path_tezheng, ID + '.wav.csv')
                tezhengzhi = csv.reader(open(path_tezheng_1, 'r', encoding='utf-8'))
                t_file_list = [i for i in tezhengzhi]

                end_1 = len(t_file_list) - 1

                for i in range(start + 1):
                    t_file_list[i].insert(0, '9')  # 最前面的无音区间全部都打标签9,把它们当做正确认识来处理

                for i in range(start_1, end_1 + 1):
                    t_file_list[i].insert(0, '9')

                l_jieguo_1.pop(-1)#最后句号的部分已经打过标签了，需要把它pop掉

                print("ID")
                print(ID)

                print("l_biaozhi")
                print(l_biaozhi)
                print("l_jieguo_1")
                print(l_jieguo_1)

                print("dianout")
                print(dianout)

                dianout_chongzao = cz.chongzao(l_biaozhi, l_jieguo_1, dianout, ID)  # 生成新的dianoutlist,以后就靠它了

                print('dianout_chongzao')
                print(dianout_chongzao)

                #通过得到的新的list,开始打标签
                # [['災害', [3, 40], 'C'], ['で', [41, 48], 'C'], ['ござい', [49, 77], 'C'], ['ます', [78, 98], 'C'],
                #  ['から', [99, 130], 'C'], ['、', [131, 152], 'C'], ['その', [153, 177], 'C'], ['場', [178, 190], 'C'],
                #  ['で', [191, 209], 'C']]
                for i in dianout_chongzao:

                    start, end = i[1]
                    if i[2] == 'C':

                        for i in range(start, end + 1):
                            t_file_list[i].insert(0, '0')

                    else:

                        for i in range(start, end + 1):
                            t_file_list[i].insert(0, '1')

                path_xinde_tezhengzhi = os.path.join(path_xinde, ID + '.csv')

                with open(path_xinde_tezhengzhi, 'w+', encoding='utf-8') as mergen_file:
                    for i in t_file_list:
                        mergen_file.write('%s\n' % ','.join(i))

        shanchu.shanchuhang(path_xinde)  # 把有标记9的特征值全部都删除掉