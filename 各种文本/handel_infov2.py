import os
import re
import openpyxl
import csv

# 文件目录
r'''
文件结构为
C:\Users\XiaoJie\Desktop\can0001
                        |-a
                            |-keka
                            |-shixulie
                            |-a.xlsx
                        |-h
                            |-keka
                            |-shixulie
                            |-h.xlsx
'''
BASE_DIRS = r'C:\Users\a7825\Desktop\can0001'

# 识别结果的文件夹名称
OUT_DIRS = 'keka'
# 特征值的文件名称
EIGENCALUE_DIRS = 'shixulie'
# 帧数需要累加的数
FRAMES_ADD = 9
# 合并后的特征值文件输出目录：
EIGENCALUE_OUT_DIRS = r'C:\Users\a7825\Desktop\can0001'


# 处理识别结果文件
def read_out(file_path):
    """
    解析out文件中的数据，
    :param file_path: out文件的路径
    :return: list [[识别结果, [帧数， 帧数], ... ]
    """
    # 打开识别几个的文件
    text_file = open(file_path, 'r', encoding='utf-8')
    text = text_file.read()
    info_list = []  # {'值': [1,9]}
    # 解析出来带【】部分的内容
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


# 生成正解文件对应关系的字典
def generate_corresponding_dict(dirs):
    """
        # 生成以下数据结构
        '''
            {
                a:[
                    {'识别出来的文字':{out_file:识别出来的文件, t:特征值文件}
                    {'识别出来的文字':{out_file:识别出来的文件, t:特征值文件}
                ]
                h:[
                    {'识别出来的文字':{out_file:识别出来的文件, t:特征值文件}
                    {'识别出来的文字':{out_file:识别出来的文件, t:特征值文件}
                ]
            }
        '''
    :param dirs: 目录
    :return:
    """
    base_dirs = dirs
    # 文件对应关系
    corresponding_dict = {}
    for per_dirs in os.listdir(base_dirs):  # per_dirs = a
        corresponding_dict[per_dirs] = []
        # 正解文件
        result_excel = os.path.join(dirs, per_dirs, '%s.xlsx' % per_dirs)
        # 处理excel
        workbook = openpyxl.load_workbook(result_excel)
        worksheet = workbook.active
        for i in worksheet.rows:
            # c1 ：编号A01， result_text： 正解文件的每句话
            cl, result_text = [a.value for a in i]
            cl = strQ2B(cl.strip()).lower()
            corresponding_dict[per_dirs].append(
                {result_text: {'out_file': os.path.join(base_dirs, per_dirs, OUT_DIRS, '%s.out' % cl),
                               't': os.path.join(base_dirs, per_dirs, EIGENCALUE_DIRS, '%s.wav.csv' % cl)}})
    return corresponding_dict


def handel_main(corresponding_dict):
    for cl in corresponding_dict:
        # 类集输出的文件名
        cl_file_path = os.path.join(EIGENCALUE_OUT_DIRS, '%s.csv' % cl)
        with open(cl_file_path, 'w+', encoding='utf-8') as mergen_file:
            for cor_dict in corresponding_dict[cl]:
                # 正解 あらゆる/現実/を/すべて/自分/の/ほう/へ/ねじ曲げ/た/の/だ/。
                result_text = list(cor_dict.keys())[0]

                # 特征值文件路径
                t_file = cor_dict[result_text]['t']

                # 识别结果文件路径
                out_file = cor_dict[result_text]['out_file']
                print('--------------',os.path.split(out_file)[-1])
                # 解析出来的识别结果 [['', [9, 22]], ['一', [23, 40]], ['週間', [41, 103]], ['ばかり', [104, 142]], ['ニューヨーク', [143, 208]], ['を', [209, 216]], ['取材', [217, 258]], ['し', [259, 276]], ['た', [277, 301]], ['。', [302, 315]]]
                out_list = read_out(out_file)
                # 弹出语句空白的部分
                start = out_list.pop(0)[1][1]

                # 特征值文件转换的list
                t_file_list = csv_to_list(t_file)
                # 语音识别空白部分去正解文件的对应行数打0标签
                for i in range(start + 1):
                    t_file_list[i].insert(0, '0')

                # 正解文件切割成列表进行遍历
                for index, item in enumerate(result_text.split('/')):
                    if len(result_text.split('/')) != len(out_list):
                        input('切割有问题:%s' % result_text)
                        break
                    # 其实帧数， 结束帧数
                    start, end = out_list[index][1]
                    # 正解文件切割的当前字符
                    a = item.strip()
                    # out文件中切割的当前字符
                    b = out_list[index][0].strip()
                    if a == b:
                        # 对比成功
                        print('[+]对比成功:%s-----%s' % (a, b))
                        # 根据帧数去正解文件中打标签
                        for i in range(start, end + 1):
                            t_file_list[i].insert(0, '0')
                    else:
                        print('[-]对比失败:%s-----%s' % (a, b))
                        # 对比失败
                        for i in range(start, end + 1):
                            t_file_list[i].insert(0, '1')
                # 处理完的正解文件列表写入合并的csv文件
                for i in t_file_list:
                    mergen_file.write('%s\n' % ','.join(i))


if __name__ == '__main__':
    handel_main(generate_corresponding_dict(BASE_DIRS))