#用CCSCC那种记号来照合正解文
import re,os,csv
import b_pipei as pi
import dahebing.muluzai as mulu
import dahebing.strQ2B as strQ2B
import dahebing.make_kana_convertor as make_kana_convertor
import dahebing.chongzao_1 as cz
import xinlaidu as xd
import yuce as yucezhi
import zhenshi

#为了处理那些因为表示方式不同而被打错标签的单词，先把错误单词的索引找出，再把单词转变成字母，然后再比较

from pykakasi import kakasi#把单词转化为音素

path=r'C:\Users\a7825\Desktop\新建文件夹 (6)'

fazhi = 0.5

# name_tezheng =
# 装有特征值的那个文件的文件名

# xinde =
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

    # path_tezheng = os.path.join(path_1, name_tezheng)

    biaozhiwenjian = csv.reader(open(os.path.join(path_1, name1), 'r', encoding='EUC-JP'))  # 把标志文件读进来
    #biaozhiwenjian = csv.reader(open(os.path.join(path_1, name2), 'r', encoding='utf-8')) #如果标志文件是.txt文件

    biaozhiwenjian_1 = [i for i in biaozhiwenjian]  # 转化为list,但是内容是list里面套list
    #[['id: l_8840_9810_T1_F_01'],['REF:  そう です か 、 はい 。 '],['HYP:  そう です か    はい 。 '],['EVAL: C    C    C  D  C    C  '],[],['id: l_10800_13190_T1_F_01']]

    # path_xinde = os.path.join(path_1, xinde)
    # mulu.mkdir(path_xinde)

    for i in range(0, len(biaozhiwenjian_1)):  # 这里的每一轮可以产生一个

        try:
            biaozhi = biaozhiwenjian_1[i][0]

        except:

            continue

        if 'id:' in biaozhi:

            l_zhengjie_1 = []
            l_jieguo_1 = []

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
                    l_zhengjie_1.append(l_zhengjie[jishuqi_zhengjie])
                    l_jieguo_1.append('')#发生删除错误，就在识别结果的列表里面加上一个空格
                    jishuqi_zhengjie += 1
                    jishuqi_biaozhi += 1

                if i == "C":#正解
                    l_zhengjie_1.append(l_zhengjie[jishuqi_zhengjie])
                    #正确的话就在识别结果和正解文两个列表里面都加入单词
                    l_jieguo_1.append(l_jieguo[jishuqi_jieguo])#
                    jishuqi_zhengjie += 1
                    jishuqi_jieguo += 1
                    jishuqi_biaozhi += 1

                if i == "I":#插入错误
                    l_jieguo_1.append(l_jieguo[jishuqi_jieguo])
                    l_zhengjie_1.append('')#发生插入错误，就在正解文的里面加入空格
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

                        l_biaozhi[jishuqi_biaozhi] = 'C'

                    jishuqi_biaozhi += 1
                    jishuqi_zhengjie += 1
                    jishuqi_jieguo += 1

            path_out_1 = os.path.join(path_out, ID + '.out')#读出.out文件
            dianout = pi.read_out(path_out_1)

            print("ID")
            print(ID)

            print("l_biaozhi")
            print(l_biaozhi)
            print("l_jieguo_1")
            print(l_jieguo_1)

            print("dianout")
            print(dianout)

            dianout.pop(0)#记住，在把.out的list放出重造函数之前要把开头的那个空白pop掉

            dianout_chongzao = cz.chongzao(l_biaozhi, l_jieguo_1, dianout, ID)  # 生成新的dianoutlist,以后就靠它了

            print('dianout_chongzao')
            print(dianout_chongzao)

            dianout_chongzao_1 = xd.read_out(dianout_chongzao,path_out_1)#往list里面加信赖度

            print('dianout_chongzao_1')

            print(dianout_chongzao_1)

            #通过得到的新的list,开始打标签
            # [['災害', [3, 40], 'C'], ['で', [41, 48], 'C'], ['ござい', [49, 77], 'C'], ['ます', [78, 98], 'C'],['から', [99, 130], 'C'], ['、', [131, 152], 'C'], ['その', [153, 177], 'C'], ['場', [178, 190], 'C'],['で', [191, 209], 'C']]
            # for i in dianout_chongzao:

            # yuce = yucezhi.yucezhi(dianout_chongzao_1,fazhi)#根据阀值取得预测值

            zhen = zhenshi.zhenshi(dianout_chongzao_1)