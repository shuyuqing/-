import os
import re
FRAMES_ADD = 1

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
    info_list_1 = []
    info = ''
    # 解析出来带[]部分的内容
    for i in re.findall(r'\[.*\]', text):

        # print (re.findall(r'\[.*\]', text))
        # 这里的话\就相当于/，在[的前面加上\就相当于我要匹配"["
        # 这里的.匹配除了换行符之外的所有东西
        # *是重复的意思，例如，ca*t 将匹配 'ct' (0个 'a' 字符)，'cat' (1个``'a')，` `'caaat' (3个 'a' 字符)，等等。
        # findall返回的是一个列表
        # split()会返回分割后的字符串列表。

        # print(i)
        # os.system("pause")


        # "+的"意思是大于等于一个
        # os.system("pause")
        # (?P<value>\s+\d+\s+\d+),这里使用了捕获组来获取[]里面的值



        try:
            info = [int(i) + FRAMES_ADD - 1 for i in re.match(r'\[(?P<value>\s+\d+\s+\d+)\]',i).group('value').split()]
            #match只匹配开头部分,函数group()可以返回被匹配到的字符串


        except:
            info = [int(i) + FRAMES_ADD - 1 for i in re.match(r'\[(?P<value>\d+\s+\d+)\]', i).group('value').split()]

        # print(info)
        # os.system("pause")

        info_list_1 = [re.search(r'\s+\[(?P<value>.*)\]', i).group('value'), info]
        #(?P<value>.*)是命名捕获组，value是这个捕获组的名称
        # 这里使用捕获组来获取了[]里面的文字
        #match是从开头开始进行匹配，而search是全部匹配


        # print(info_list_1)
        # os.system("pause")

        info_list.append(info_list_1)
        # print(i)

    # print(info_list)
    return info_list
    #最后的效果:[['', [0, 18]], ['お', [19, 24]], ['願い', [25, 49]], ['三', [50, 82]], ['。', [83, 86]]]

    #[  37   58]  0.562999  で+接続詞	[で]





