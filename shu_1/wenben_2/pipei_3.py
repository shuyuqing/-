# 用CCSCC那种记号来照合正解文
import re, os, csv
import pipei as pi
from pykakasi import kakasi

# 打标签的思路是：因为CCSS的符号是跟正解文对应的，跟识别结果不对应，这个是最大的难点，所以要做的是先去找标志文件里面的C,
# 也就是正确认识的部分，然后返回这些C的索引，然后根据索引去正解文中找被正确识别的单词，找到之后把单词顺序插入到一个list中去，
# 在用识别结果里的单词去对应这个list,按顺序一个单词一个单词地对，每成功对应上一个单词就从list中把这个单词删除掉，并获取这个单词
# 的帧数表，然后打上标签0，没有对应上的单词就在这个单词的范围内打上标签1

BASE_DIRS = r'C:\Users\a7825\Desktop\工作空间\语音数据\UUDB\第一次实验\打标签\第一批'
# 主要文件的路径

name = 'symbol.txt'
# 表记着CCCCSSSS标志的文件

name_tezheng = 'log'
# 装有特征值的那个文件的文件名

houzhui = '.wav.csv'
# 特征值文件中除去id号之后的后缀部分

tezhengzhi = 'log'
# 特征值文件的名字

xinde = 'xinde'
# 装入新的特征值的文件名

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

shibie = {}


# 识别结果词典

# 这是一个字典，字典里面的每一个元素都是一个list

# if 'id' in i[0]:
#     print(i[0])
# if 'EVAL:' in i[0]:
#     print(i[0])


def csv_to_list(csv_path):  # 把数据读入并转换为列表
    a = csv.reader(open(csv_path, 'r', encoding='utf-8'))
    return [i for i in a]


def zidian(dir):  # 建立三个字典

    txtwenjian = csv.reader(open(os.path.join(BASE_DIRS, dir, name), 'r', encoding='cp932',
                                 errors='ignore'))  # 把symbol标志文件读进来,编码有问题的话就用encoding='utf-8'

    banyun = ''

    b = [i for i in txtwenjian]  # 转化为list

    for q in b:
        if q != []:
            if 'id' in q[0]:
                banyun = q[0]  # 标志文件里面有文件名
                # print(q[0])  # 这里的id就是文件名

            if 'EVAL' in q[0]:
                s = q[0].split()
                s.pop(0)  # 把列表的第一个元素pop掉

                while 'I' in s:
                    s.remove('I')  # 一次性只会删除一个I,所以要用while,很多时候是因为I，符号的个数比正解文的单词数还要多
                # print(len(s))
                # os.system("pause")
                symbolcidian[banyun.replace('id: ', '')] = s  # 把符号放入字典

            if 'REF' in q[0]:
                s = q[0].split()
                s.pop(0)
                # print(len(s))
                # print(s)
                zhengjie[banyun.replace('id: ', '')] = s  # 正解文

            if 'HYP' in q[0]:
                s = q[0].split()
                s.pop(0)
                # print(s)
                shibie[banyun.replace('id: ', '')] = s  # 识别结果

        else:
            pass
    # print("正解")
    # print(zhengjie)
    # print(symbolcidian)
    # print("识别结果")
    # print(shibie)

    return zhengjie, symbolcidian


if __name__ == '__main__':

    kakasi = kakasi()
    kakasi.setMode("H", "a")  # Hiragana to ascii, default: no conversion
    kakasi.setMode("K", "a")  # Katakana to ascii, default: no conversion
    kakasi.setMode("J", "a")  # Japanese to ascii, default: no conversion
    kakasi.setMode("r", "Hepburn")  # default: use Hepburn Roman table
    kakasi.setMode("s", True)  # add space, default: no separator

    for per_dirs in os.listdir(BASE_DIRS):  # per_dirs = C001L,C001R...

        zhengjie, symbolcidian = zidian(per_dirs)
        # 从标志文件中把标志塞进symbolcidian字典里

        for id in os.listdir(os.path.join(BASE_DIRS, per_dirs, name_tezheng)):  # id = C001L,C001R下面的文件的名字

            banyun_1 = []  # 存储C的索引
            banyun_2 = []  # 存储正确的单词

            banyun_3 = []  # 存储非C的索引
            banyun_4 = []  # 存储暂时不正确的单词
            dianout = []

            id = id.replace(houzhui, '')  # 把文件名中的.wav.csv去掉只剩id

            # print(id)
            # print(symbolcidian[id])

            enumerate(symbolcidian[id])

            banyun_1 = [i for i, x in enumerate(symbolcidian[id]) if x == 'C']  # 返回标志C的索引
            banyun_3 = [i for i, x in enumerate(symbolcidian[id]) if x != 'C']

            t_file = os.path.join(BASE_DIRS, per_dirs, tezhengzhi, id + houzhui)
            t_file_list = csv_to_list(t_file)  # 把特征值文件转化为list

            if len(banyun_1) == 0:  # 如果没有一个是正确的，全错，所有的数据都打标签1
                for i in range(len(t_file_list)):
                    t_file_list[i].insert(0, '1')


            else:
                for u in banyun_1:  # banyun_1里面装的全是标志C的索引

                    if u + 1 <= len(zhengjie[id]):  # 正解文单词的个数可能没有标志的个数多
                        # print(banyun_1)
                        # print(zhengjie[id][u])
                        # print(zhengjie[id])
                        # print("已经把正确单词 %s 加入数组"%str(zhengjie[id][u]))
                        banyun_2.append(zhengjie[id][u])
                    else:  # 如果C标志的索引号大于正解文单词的索引号，那就只能手动去调整了
                        print("手动调一下这个文件吧%s" % id)
                        print("它的正确单词是")
                        print(banyun_2)
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

                start = dianout.pop(0)[1][1]

                # print(start)

                for i in range(start + 1):
                    t_file_list[i].insert(0, '0')  # 最前面的无音区间全部都打标签0,把它们当做正确认识来处理

                for y in dianout:  # dianout是识别结果跟对应的帧数表

                    # print("此时的单词是%s"%y)
                    # print("此时的匹配结果是")
                    # print(dianout)
                    # os.system("pause")

                    if y[1][1] + 1 <= len(t_file_list):  # 判断这个单词的范围是否超出了特征值得总行数

                        if y[0] == '':
                            continue
                        if y[0] in banyun_2:  # 如果这个单词存在列表banyun_2中，就给这个单词对应的帧数范围打标签0
                            start, end = y[1]
                            print("正在为文件 %s 的单词 %s 打标签" % (os.path.split(dir_out)[1], y[0]))
                            for i in range(start, end + 1):
                                t_file_list[i].insert(0, '0')
                            banyun_2.remove(y[0])  # 打完标签0之后再从列表中把这个单词删


                        else:
                            start, end = y[1]  # 如果这个单词不在列表banyun_2中，就给这个单词对应的帧数范围打标签1
                            print("正在为文件 %s 的单词 %s 打标签" % (os.path.split(dir_out)[1], y[0]))
                            for i in range(start, end + 1):
                                t_file_list[i].insert(0, '1')

                    elif y[1][1] + 1 > len(t_file_list):

                        if y[0] == '':
                            continue
                        if y[0] in banyun_2:
                            start = y[1][0]
                            end = len(t_file_list)  # 如果这个单词的帧数表的范围超出了特征值得行数，就以特征值行数作为end
                            print("正在为文件 %s 的单词 %s 打标签" % (os.path.split(dir_out)[1], y[0]))
                            for i in range(start, end):
                                t_file_list[i].insert(0, '0')
                            banyun_2.remove(y[0])
                        else:
                            start = y[1][0]
                            end = len(t_file_list)
                            print("正在为文件 %s 的单词 %s 打标签" % (os.path.split(dir_out)[1], y[0]))
                            for i in range(start, end):
                                t_file_list[i].insert(0, '1')

            with open(os.path.join(BASE_DIRS, per_dirs, xinde, id + '.csv'), 'w+', encoding='utf-8') as mergen_file:
                for i in t_file_list:
                    mergen_file.write('%s\n' % ','.join(i))

            # os.system("pause")

            # 请参看pipei.py



