#用CCSCC那种记号来照合正解文
import re,os,csv
import pipei as pi
from pykakasi import kakasi#把平假名或片假名转化为读音
import muluzai as mulu
import shanchuhang_2 as shanchu#为了除去那些被打上标签9的特征值
import zidian
import strQ2B
import make_kana_convertor

#打标签的思路是：因为CCSS的符号是跟正解文,识别结果两个中比较长的一个对应的，这个是最大的难点，所以要做的是先去找标志文件里面的C,
#也就是正确认识的单词，然后返回这些C的索引，然后根据索引去识别结果(正解文)中找被正确识别的单词，注意只有识别结果才对应帧数表，找到之后把单词顺序插入到一个list中去，
#在用识别结果里的单词去对应这个list,按顺序一个单词一个单词地对，每成功对应上一个单词就从list中把这个单词删除掉，并获取这个单词
#的帧数表，然后打上标签0，没有对应上的单词就在这个单词的范围内打上标签1
#为了处理那些因为表示方式不同而被打错标签的单词，先把错误单词的索引找出，再把单词转变成字母，然后再比较

def dabiaoqian(path):

    from pykakasi import kakasi
    import csv, os

    name_tezheng = 'log'
    # 装有特征值的那个文件的文件名

    xinde = 'xinde_log'
    # 装入新的特征值的文件名

    houzhui = '.wav.csv'
    # 特征值文件中除去id号之后的后缀部分

    name = 'align1'
    # 表记着CCCCSSSS标志的文件

    name1 = 'align1'
    name2 = 'align1.txt'

    shibiejieguo = {}
    # 安放识别结果的字典

    symbolcidian = {}
    # 这样的词典,标志词典
    # id: C001L_086
    # ['S', 'S', 'S', 'C', 'S', 'D', 'D', 'D', 'C']
    # id: C001L_087
    # ['S', 'D', 'D', 'C']
    # id: C001L_088
    # ['S', 'S', 'S', 'S', 'D', 'D', 'D', 'D', 'C', 'C']
    zhengjie = {}
    # 正解文词典
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

        biaozhiwenjian = csv.reader(open(os.path.join(path_1, name1), 'r', encoding='EUC-JP'))  # 把标志文件读进来
        # biaozhiwenjian = csv.reader(open(os.path.join(path_1, name2), 'r', encoding='utf-8')) #如果标志文件是.txt文件

        biaozhiwenjian_1 = [i for i in biaozhiwenjian]  # 转化为list,但是内容是list里面套list
        #[['id: l_8840_9810_T1_F_01'],['REF:  そう です か 、 はい 。 '],['HYP:  そう です か    はい 。 '],['EVAL: C    C    C  D  C    C  '],[],['id: l_10800_13190_T1_F_01']]

        # print(biaozhiwenjian_1)
        # os.system('pause')

        path_xinde = os.path.join(path_1, xinde)
        mulu.mkdir(path_xinde)

        for i in range(0,len(biaozhiwenjian_1),5):#这里的每一轮可以为一个语音文件打标签

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

            # try:
            #     ID = biaozhiwenjian_1[i].replace('id: ', '')
            #
            #     l_zhengjie = biaozhiwenjian_1[i+1].split()
            #     l_zhengjie.pop(0)
            #
            #     l_jieguo = biaozhiwenjian_1[i+2].split()
            #     l_jieguo.pop(0)
            #
            #     l_biaozhi = biaozhiwenjian_1[i+3].split()
            #     l_biaozhi.pop(0)
            #
            # except:
            #     print(biaozhiwenjian_1[i])
            #     os.system("pause")

            #建立严格对应的正解，识别结果，标记，如果标记是d的话，结果就是空
            jishuqi_jieguo = 0
            jishuqi_zhengjie = 0

            for i in l_biaozhi:

                if i == "D":
                    l_zhengjie_1.append(l_zhengjie[jishuqi_zhengjie])
                    l_jieguo_1.append('')
                    jishuqi_zhengjie += 1

                if i == "C":
                    l_zhengjie_1.append(l_zhengjie[jishuqi_zhengjie])
                    l_jieguo_1.append(l_jieguo[jishuqi_jieguo])
                    jishuqi_zhengjie += 1
                    jishuqi_jieguo += 1

                if i == "I":
                    l_jieguo_1.append(l_jieguo[jishuqi_jieguo])
                    l_zhengjie_1.append('')
                    jishuqi_jieguo += 1

                if i == "S":
                    l_zhengjie_1.append(l_zhengjie[jishuqi_zhengjie])
                    l_jieguo_1.append(l_jieguo[jishuqi_jieguo])
                    jishuqi_zhengjie += 1
                    jishuqi_jieguo += 1

            # print(l_jieguo_1)
            # print(l_zhengjie_1)
            # print(l_biaozhi)
            # os.system('pause')

            path_out_1 = os.path.join(path_out, ID + '.out')
            dianout = pi.read_out(path_out_1)

            # print(dianout)
            # os.system('pause')

            path_tezheng_1 = os.path.join(path_tezheng, ID + '.wav.csv')
            tezhengzhi = csv.reader(open(path_tezheng_1, 'r', encoding='utf-8'))
            t_file_list = [i for i in tezhengzhi]
            dimension = len(t_file_list[0])

            start = dianout.pop(0)[1][1]#给开始的无音区间打标签9

            for i in range(start + 1):
                t_file_list[i].insert(0, '9')  # 最前面的无音区间全部都打标签9,把它们当做正确认识来处理

            zhenshubiao = {}#给每个单词都建立一个词典

            for i in dianout:
                zhenshubiao[i[0]] = i[1]#一个.out文件中的每个单词都建立一个对应的字典

            start,end = zhenshubiao['。']#给最后面的句号的部分打上标签9

            for i in range(start, end + 1):
                t_file_list[i].insert(0, '9')

            # print(dianout)
            # os.system('pause')
            # 最后的效果:[['', [0, 18]], ['お', [19, 24]], ['願い', [25, 49]], ['三', [50, 82]], ['。', [83, 86]]]
            # while 'D' in l_biaozhi:
            #     l_biaozhi.remove('D')  # 一次性只会删除一个D,所以要用while

            l_biaozhi_1 = [i for i, x in enumerate(l_biaozhi) if x == 'S']  # 返回标志S的索引
            # print(len(l_biaozhi_1))
            # os.system('pause')

            if len(l_biaozhi_1) != 0:#如果l_biaozhi_1里面没有单词，说明全部都被正确认识了

                # print('l_jieguo_1')
                # print(l_jieguo_1)
                #
                # print('l_biaozhi_1')
                # print(l_biaozhi_1)
                #
                # print('l_biaozhi')
                # print(l_biaozhi)
                #
                # print('l_zhengjie_1')
                # print(l_zhengjie_1)

                # print(l_jieguo_1)
                # print(l_zhengjie_1)
                # print(l_biaozhi)

                for y in l_biaozhi_1:#处理标志s对应的单词,把正解文和识别结果都转化为字母再比较一次
                    # print("现在输出y的值")
                    # print(y)
                    #
                    # print('现在输出l_jieguo_1[y]')
                    # print(l_jieguo_1[y])
                    # print(ID)
                    # os.system('pause')

                    #先处理识别结果
                    if conv.do(l_jieguo_1[y]) == l_jieguo_1[y] and l_jieguo_1[y] != '、':#判断是不是字母

                        try:
                            zhuanhuan_jieguo = conv.do(make_kana_convertor._make_kana_convertor(strQ2B.strQ2B(l_jieguo_1[y])))

                        except:
                            zhuanhuan_jieguo = conv.do(make_kana_convertor._make_kana_convertor(l_jieguo_1[y]))

                    else:
                        zhuanhuan_jieguo = conv.do(l_jieguo_1[y])

                    #再处理正解文
                    if conv.do(l_zhengjie_1[y]) == l_zhengjie_1[y] and l_zhengjie_1[y] != '、':  # 判断是不是字母

                        try:
                            zhuanhuan_zhengjie = conv.do(make_kana_convertor._make_kana_convertor(strQ2B.strQ2B(l_zhengjie_1[y])))

                        except:
                            zhuanhuan_zhengjie = conv.do(make_kana_convertor._make_kana_convertor(l_zhengjie_1[y]))

                    else:
                        zhuanhuan_zhengjie = conv.do(l_zhengjie_1[y])

                    # print('l_jieguo_1[y]')
                    # print(l_jieguo_1[y])
                    # os.system('pause')

                    guanjianzi = l_jieguo_1[y]#把S对应的单词取出来

                    # print('guanjianzi')
                    # print(guanjianzi)
                    # os.system('pause')
                    #
                    # print('zhenshubiao')
                    # print(zhenshubiao[guanjianzi])
                    # os.system('pause')

                    try:
                        start,end = zhenshubiao[guanjianzi]#把这个单词对应的帧数范围取出来

                    except:
                        print('ID')
                        print(ID)
                        print('zhenshubiao')
                        print(zhenshubiao)
                        print('guanjianzi')
                        print(guanjianzi)
                        os.system('pause')

                    for i in range(start, end + 1):

                        if zhuanhuan_jieguo == zhuanhuan_zhengjie:
                            t_file_list[i].insert(0, '0')

                        else:
                            t_file_list[i].insert(0, '1')

            jishuqi_tezhengzhi = 0

            for i in t_file_list:#给被正确识别的单词打标签0

                # if i[0] != '0' and i[0] != '1' and i[0] != '9':

                if len(i[0])  == dimension:
                    t_file_list[jishuqi_tezhengzhi].insert(0, '0')

                jishuqi_tezhengzhi += 1

            path_xinde_tezhengzhi = os.path.join(path_xinde,ID + '.csv')

            with open(path_xinde_tezhengzhi, 'w+', encoding='utf-8') as mergen_file:
                for i in t_file_list:
                    mergen_file.write('%s\n' % ','.join(i))

        shanchu.shanchuhang(path_xinde)  # 把有标记9的特征值全部都删除掉