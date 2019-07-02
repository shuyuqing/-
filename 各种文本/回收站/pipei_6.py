# 用CCSCC那种记号来照合正解文
import re, os, csv
import pipei as pi
from pykakasi import kakasi  # 把平假名或片假名转化为读音
import muluzai as mulu
import shanchuhang_2 as shanchu  # 为了除去那些被打上标签9的特征值
import zidian
import strQ2B
import make_kana_convertor
# 打标签的思路是：因为CCSS的符号是跟正解文,识别结果两个中比较长的一个对应的，这个是最大的难点，所以要做的是先去找标志文件里面的C,
# 也就是正确认识的单词，然后返回这些C的索引，然后根据索引去识别结果(正解文)中找被正确识别的单词，注意只有识别结果才对应帧数表，找到之后把单词顺序插入到一个list中去，
# 在用识别结果里的单词去对应这个list,按顺序一个单词一个单词地对，每成功对应上一个单词就从list中把这个单词删除掉，并获取这个单词
# 的帧数表，然后打上标签0，没有对应上的单词就在这个单词的范围内打上标签1
# 为了处理那些因为表示方式不同而被打错标签的单词，先把错误单词的索引找出，再把单词转变成字母，然后再比较

def dabiaoqian(path):
    from pykakasi import kakasi

    BASE_DIRS = path
    # 批次

    name_tezheng = 'mizhichuli_log'
    # 装有特征值的那个文件的文件名

    xinde = 'xinde_mizhichuli'
    # 装入新的特征值的文件名

    houzhui = '.wav.csv'
    # 特征值文件中除去id号之后的后缀部分

    name = 'align1'
    # 表记着CCCCSSSS标志的文件

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

    for per_dirs in os.listdir(BASE_DIRS):  # per_dirs = C001L,C001R...

        d_9 = os.path.join(BASE_DIRS, per_dirs, xinde)
        d = os.path.join(BASE_DIRS, per_dirs, xinde)
        mulu.mkdir(d)

        zhengjie, symbolcidian = zidian.zidian(per_dirs,BASE_DIRS)
        # 从标志文件中把标志塞进symbolcidian字典里

        for id in os.listdir(os.path.join(BASE_DIRS, per_dirs, name_tezheng)):  # id = C001L,C001R下面的文件的名字

            banyun_1 = []  # 存储C的索引
            banyun_2 = []  # 存储正确的单词

            banyun_3 = []  # 存储非C的索引
            banyun_4 = []  # 存储暂时不正确的单词的拼音
            dianout = []

            id = id.replace(houzhui, '')  # 把文件名中的.wav.csv去掉只剩id

            # print(id)
            # print(symbolcidian[id])

            enumerate(symbolcidian[id])

            banyun_1 = [i for i, x in enumerate(symbolcidian[id]) if x == 'C']  # 返回标志C的索引
            banyun_3 = [i for i, x in enumerate(symbolcidian[id]) if x == 'S']  # 返回替换错误的单词的索引

            t_file = os.path.join(BASE_DIRS, per_dirs, name_tezheng, id + houzhui)
            a = csv.reader(open(t_file, 'r', encoding='utf-8'))
            t_file_list = [i for i in a]

            # if len(banyun_1) == 0:#如果没有一个是正确的，全错，所有的数据都打标签1
            #     for i in range(len(t_file_list)):
            #         t_file_list[i].insert(0, '1')
            # print(banyun_1)
            # print(banyun_3)
            # os.system("pause")

            for u in banyun_1:  # banyun_1里面装的全是标志C的索引

                if u + 1 <= len(zhengjie[id]):  # 正解文单词的个数可能没有标志的个数多
                    # print(banyun_1)
                    # print(zhengjie[id][u])
                    # print(zhengjie[id])
                    # print("已经把正确单词 %s 加入数组"%str(zhengjie[id][u]))
                    banyun_2.append(zhengjie[id][u])  # banyun_2是存储正确单词的索引的数组
                    # print("此时的banyun_2是")
                    # print(banyun_2)
                    # os.system('pause')
                else:  # 如果C标志的索引号大于正解文单词的索引号，那就只能手动去调整了
                    print("手动调一下这个文件吧%s" % id)
                    print("它的正确单词是")
                    print(banyun_2)
                    os.system("pause")
            # print(banyun_2)
            # os.system('pause')

            for w in banyun_3:  # 存储非C的索引

                if w + 1 <= len(zhengjie[id]):  # 正解文单词的个数可能没有标志的个数多

                    result = conv.do(zhengjie[id][w])
                    banyun_4.append(result)
                    # if result == zhengjie[id][w] and zhengjie[id][w] != '、':#如果是逗号，也按正常的单词处理
                    #
                    #     banyun_4.append(conv.do(_make_kana_convertor(strQ2B(zhengjie[id][w]))))#如果转化之后的值不变，就说明遇到了字母，把字母转化为半角，再再转化为片假名,之后再转化为罗马字加入列表中
                    # else:
                    # #     banyun_4.append(result)#存储暂时不正确的单词
                    # print("此时的banyun_4是")
                    # print(banyun_4)
                    # os.system('pause')

                else:  # 如果C标志的索引号大于正解文单词的索引号，那就只能手动去调整了
                    print("手动调一下这个文件吧%s" % id)
                    print("它的认识出现错误的单词是")
                    print(banyun_4)
                    os.system("pause")

                # print(banyun_2)
                # os.system("pause")

            # for p in symbolcidian[id]:
            #     os.system("pause")
            #     # while p == 'C':
            #     print(p.index('C'))

            dir_out = os.path.join(BASE_DIRS, per_dirs, 'keka', id + '.out')
            dianout = pi.read_out(dir_out)  # 提取出来的帧号跟julius识别结果一样
            # print(dianout)
            # os.system('pause')
            # 最后的效果:[['', [0, 18]], ['お', [19, 24]], ['願い', [25, 49]], ['三', [50, 82]], ['。', [83, 86]]]

            # [  37   58]  0.562999  で+接続詞	[で]
            start = dianout.pop(0)[1][1]

            # print(start)

            for i in range(start + 1):
                t_file_list[i].insert(0, '9')  # 最前面的无音区间全部都打标签9,把它们当做正确认识来处理

            for y in dianout:  # dianout是识别结果跟对应的帧数表

                # print("此时的单词是%s"%y)
                # print("此时的匹配结果是")
                # print(dianout)
                # os.system("pause")

                if y[1][1] + 1 <= len(t_file_list):  # 判断这个单词的范围是否超出了特征值得总行数

                    if y[0] == '':  # 跳过前面的无音区
                        continue

                    if y[0] == dianout[-1][0]:  # 这段代码是为了把最后句号的部分全部打上标签9而设置的注意一下，下面也有一段代码
                        start, end = y[1]
                        for i in range(start, end + 1):
                            t_file_list[i].insert(0, '9')
                        continue

                    if y[0] in banyun_2:  # 如果这个单词存在列表banyun_2中，就给这个单词对应的帧数范围打标签0
                        start, end = y[1]
                        print("正在为文件 %s 的单词 %s 打标签" % (os.path.split(dir_out)[1], y[0]))
                        for i in range(start, end + 1):
                            t_file_list[i].insert(0, '0')
                        banyun_2.remove(y[0])  # 打完标签0之后再从列表中把这个单词删掉

                    elif conv.do(y[0]) == y[0] and y[0] != '、':  # 如果是字母的话，转化之后还是字母

                        print("发现识别结果中的字母%s" % y[0])
                        print("它在文件%s" % dir_out)

                        try:
                            zhuanhuazhi = conv.do(make_kana_convertor._make_kana_convertor(strQ2B.strQ2B(y[0])))

                        except:
                            zhuanhuazhi = conv.do(make_kana_convertor._make_kana_convertor(y[0]))

                        if zhuanhuazhi in banyun_4:  # 需要先把字母转化为片假名然后再转化为读音
                            print("转化之后的字母为%s" %zhuanhuazhi)
                            # os.system('pause')
                            start, end = y[1]
                            print("正在为文件 %s 的单词 %s 打标签" % (os.path.split(dir_out)[1], y[0]))
                            for i in range(start, end + 1):
                                t_file_list[i].insert(0, '0')
                            banyun_4.remove(conv.do(
                                zhuanhuazhi))  # 打完标签0之后再从列表中把这个单词删掉
                        else:
                            start, end = y[1]
                            print("正在为文件 %s 的单词 %s 打标签" % (os.path.split(dir_out)[1], y[0]))
                            for i in range(start, end + 1):
                                t_file_list[i].insert(0, '1')

                    elif conv.do(y[0]) in banyun_4:
                        start, end = y[1]
                        print("正在为文件 %s 的单词 %s 打标签" % (os.path.split(dir_out)[1], y[0]))
                        for i in range(start, end + 1):
                            t_file_list[i].insert(0, '0')
                        banyun_4.remove(conv.do(y[0]))  # 打完标签0之后再从列表中把这个单词删掉

                    else:
                        start, end = y[1]  # 如果这个单词不在列表banyun_2中，就给这个单词对应的帧数范围打标签1
                        print("正在为文件 %s 的单词 %s 打标签" % (os.path.split(dir_out)[1], y[0]))
                        for i in range(start, end + 1):
                            t_file_list[i].insert(0, '1')

                elif y[1][1] + 1 > len(t_file_list):

                    if y[0] == '':
                        continue

                    if y[0] == dianout[-1][0]:
                        start = y[1][0]
                        end = len(t_file_list)
                        for i in range(start, end):  # 如果是y[1][1]+1 > len(t_file_list)的情况这里end就不能加一了
                            t_file_list[i].insert(0, '9')
                        continue
                    # 这段代码是为了把最后句号的部分全部打上标签9而设置的注意一下，上面也有一段代码

                    if y[0] in banyun_2:
                        start = y[1][0]
                        end = len(t_file_list)  # 如果这个单词的帧数表的范围超出了特征值得行数，就以特征值行数作为end
                        print("正在为文件 %s 的单词 %s 打标签" % (os.path.split(dir_out)[1], y[0]))
                        for i in range(start, end):
                            t_file_list[i].insert(0, '0')
                        banyun_2.remove(y[0])

                    elif conv.do(y[0]) == y[0] and y[0] != '、':  # 如果是字母的话，转化之后还是字母

                        if conv.do(make_kana_convertor._make_kana_convertor(y[0])) in banyun_4:  # 需要先把字母转化为片假名然后再转化为读音
                            start = y[1][0]
                            end = len(t_file_list)
                            print("正在为文件 %s 的单词 %s 打标签" % (os.path.split(dir_out)[1], y[0]))
                            for i in range(start, end + 1):
                                t_file_list[i].insert(0, '0')
                            banyun_4.remove(
                                conv.do(make_kana_convertor._make_kana_convertor(y[0])))  # 打完标签0之后再从列表中把这个单词删掉

                        else:
                            start = y[1][0]
                            end = len(t_file_list)
                            print("正在为文件 %s 的单词 %s 打标签" % (os.path.split(dir_out)[1], y[0]))
                            for i in range(start, end + 1):
                                t_file_list[i].insert(0, '1')
                    else:
                        start = y[1][0]
                        end = len(t_file_list)
                        print("正在为文件 %s 的单词 %s 打标签" % (os.path.split(dir_out)[1], y[0]))
                        for i in range(start, end):
                            t_file_list[i].insert(0, '1')

            with open(os.path.join(BASE_DIRS, per_dirs, xinde, id + '.csv'), 'w+', encoding='utf-8') as mergen_file:
                for i in t_file_list:
                    mergen_file.write('%s\n' % ','.join(i))

        shanchu.shanchuhang(d_9)  # 把有标记9的特征值全部都删除掉
