#给特征值打标签的,这个是第二版，可以处理特征值的行数比识别结果的最后一个单词的最后一个帧的编号要小的情况
import os
import dabiaoqian.data_1 as data_1
import dabiaoqian.data_2 as data_2
import re
import openpyxl
import csv

# 文件目录
r'''
文件结构为
C:\Users\XiaoJie\Desktop\can0001
                    F1
                        |-a
                            |-keka
                            |-shixulie
                            |-a.xlsx
                        |-h
                            |-keka
                            |-shixulie
                            |-h.xlsx
'''
BASE_DIRS = r'C:\Users\a7825\Desktop\工作空间\语音数据\UUDB\第一次实验\打标签\第三批'

OUT_DIRS = 'keka'
# 识别结构的文件夹名称

EIGENCALUE_DIRS = 'mizhichuli'
# 特征值的文件名称

FRAMES_ADD = 2
# 帧数需要累加的数

EIGENCALUE_OUT_DIRS = r'C:\Users\a7825\Desktop\工作空间\语音数据\UUDB\第一次实验\打标签\第三批结果'
# 合并后的特征值文件输出目录：

def read_out(file_path):
    """
    解析out文件中的数据，
    :param file_path: out文件的路径
    :return: list [[识别结果, [帧数， 帧数], ... ]
    """
    # 打开识别几个的文件
    text_file = open(file_path, 'r', encoding='utf-8')
    text = text_file.read()#read()读全部,readline()读一行,readlines()读所有行
    info_list = []  # {'值': [1,9]}
    # 解析出来带[]部分的内容
    for i in re.findall(r'\[.*\]', text):
        info_list.append([re.search(r'\s+\[(?P<value>.*)\]', i).group('value'), [int(i) + FRAMES_ADD - 1 for i in
                                                                                 re.match(
                                                                                     r'\[(?P<value>\s+\d+\s+\d+)\]',
                                                                                     i).group('value').split()]])
    return info_list

# 字符串全角转半角
def strQ2B(ustring):
    """把字符串全角转半角"""
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 0x3000:
            inside_code = 0x0020
        else:
            inside_code -= 0xfee0
        if inside_code < 0x0020 or inside_code > 0x7e:  # 转完之后不是半角字符返回原来的字符
            rstring += uchar
        rstring += chr(inside_code)
    return rstring

# csv文件转换成list
def csv_to_list(csv_path):
    a = csv.reader(open(csv_path, 'r', encoding='utf-8'))
    return [i for i in a]
    #返回的是一个双层列表，第一维是特征值的行数，第二微才是具体的每一个特征值的数据


# 生成正解文件对应关系的字典
def generate_corresponding_dict(dirs):
    """
        # 生成以下数据结构,四层结构，一个字典里面有n多个list,每个list里面又有n多个字典，每个字典里面又有一个字典
        '''
            {
                a:[
                    {'第一句正解文':{out_file:识别结果的路径, t:特征值文件的路径}}
                    {'第二句正解文':{out_file:识别结果的路径, t:特征值文件的路径}}
                     。。。。。。
                ]
                h:[
                    {'第一句正解文':{out_file:识别结果的路径, t:特征值文件的路径}}
                    {'第二句正解文':{out_file:识别结果的路径, t:特征值文件的路径}}
                    。。。。。。
                ]
            }
        '''
    :param dirs: 目录
    :return:
    """
    base_dirs = dirs
    # 文件对应关系

    corresponding_dict = {}
    #这是一个字典，字典里面的每一个元素都是一个list
    for per_dirs in os.listdir(base_dirs):  # per_dirs = a，h...
        corresponding_dict[per_dirs] = []
        #字典里面的每一个元素都是一个list
        # 正解文件
        result_excel = os.path.join(dirs, per_dirs, '%s.xlsx' % per_dirs)
        # 处理excel
        workbook = openpyxl.load_workbook(result_excel)
        worksheet = workbook.active
        for i in worksheet.rows:
            # c1 ：编号A01， result_text： 正解文件的每句话
            # a,b,c = [1,2]
            # print(a)
            # print(b)
            # 输出就是1和2
            # 居然还能这样从可迭代对象里面把数据给取出来
            cl, result_text = [a.value for a in i]
            # cl = strQ2B(cl.strip()).lower()
            #可以把全角字母转换为半角
            corresponding_dict[per_dirs].append(
                {result_text: {'out_file': os.path.join(base_dirs, per_dirs, OUT_DIRS, '%s.out' % cl),
                               't': os.path.join(base_dirs, per_dirs, EIGENCALUE_DIRS, '%s.wav.csv' % cl)}})
            #result_text中包含识别结果以及特征值的文件的路径
            #居然是以正解文为key,
            #{'a': [{'あらゆる/現実/を/すべて/自分/の/ほう/へ/ねじ曲げ/た/の/だ/。': {'out_file': 'C:\\Users\\a7825\\Desktop\\工作空间\\跑代码\\数据-i\\can1001\\a\\keka\\Ａ０１.out', 't': 'C:\\Users\\a7825\\Desktop\\工作空间\\跑代码\\数据-i\\can1001\\a\\shxulie\\Ａ０１.wav.csv'}},
            # {'一/週間/ばかり/ニューヨーク/を/取材/し/た/。': {'out_file': 'C:\\Users\\a7825\\Desktop\\工作空间\\跑代码\\数据-i\\can1001\\a\\keka\\Ａ０２.out', 't': 'C:\\Users\\a7825\\Desktop\\工作空间\\跑代码\\数据-i\\can1001\\a\\shxulie\\Ａ０２.wav.csv'}}
    return corresponding_dict


def handel_main(corresponding_dict):


    for cl in corresponding_dict:#迭代字典里面的东西跟迭代list里面的东西不一样
        # 如果这里是输出cl的话，将得到a,b,c,d,也就是字典里面的key

        for cor_dict in corresponding_dict[cl]:
            # 正解 あらゆる/現実/を/すべて/自分/の/ほう/へ/ねじ曲げ/た/の/だ/。
            #list(cor_dict.keys())只是把key装在了list里面并返回了这个list,
            result_text = list(cor_dict.keys())[0]

            # 特征值文件路径
            t_file = cor_dict[result_text]['t']
            #双层字典，要输出第二层字典的内容就像二维矩阵那样输出

            # 识别结果文件路径
            out_file = cor_dict[result_text]['out_file']
            print('--------------',os.path.split(out_file)[-1])#从路径中剥离出最后一个词，这个

            # 解析出来的识别结果 [['', [9, 22]], ['一', [23, 40]], ['週間', [41, 103]], ['ばかり', [104, 142]], ['ニューヨーク', [143, 208]], ['を', [209, 216]], ['取材', [217, 258]], ['し', [259, 276]], ['た', [277, 301]], ['。', [302, 315]]]
            out_list = read_out(out_file)
            # 弹出语句空白的部分
            start = out_list.pop(0)[1][1]

            # 特征值文件转换的list
            t_file_list = csv_to_list(t_file)
            # 语音识别空白部分打0标签
            # if start>len(t_file_list):
            #     start = len(t_file_list)

            for i in range(start):
                t_file_list[i].insert(0, '0')

            # end = out_list[-1][1][1]+1
            # for i in range(end, len(t_file_list)):
            #     t_file_list[i].insert(0, '0')
                #在句尾的部分打标签0

            # 正解文件切割成列表进行遍历，item是每个单词，这些单词被/切割开了，index是该单词的序号
            for index, item in enumerate(result_text.split('/')):#result_text是一句正解文，split返回的是一个列表
                if len(result_text.split('/')) != len(out_list):#out_list是识别结果的单词
                    input('切割有问题:%s' % result_text)
                    break

                if out_list[index][1][1]<=len(t_file_list):#关键在于要找到特征值的最后一行的编号落在识别结果的哪段单词的帧数的区间里

                    t_file_list = data_1.biaoqian(out_list,item,t_file_list,index)

                else:

                    t_file_list = data_2.biaoqian(out_list,item,t_file_list,index)
                    break

            ming = os.path.split(cor_dict[result_text]['t'])

            cl_file_path = os.path.join(EIGENCALUE_OUT_DIRS, '%s.csv' %ming[1])
            with open(cl_file_path, 'w+', encoding='utf-8') as mergen_file:
                # 处理完的正解文件列表写入合并的csv文件
                for i in t_file_list:
                    mergen_file.write('%s\n' % ','.join(i))


if __name__ == '__main__':
    handel_main(generate_corresponding_dict(BASE_DIRS))
