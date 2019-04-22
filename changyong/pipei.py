import os
import re
file_path = r"C:\Users\a7825\Desktop\工作空间\杂物\用于测试打标签的文本\keka/C003L_035.out"
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
        #


        # print(i)
        # os.system("pause")

        try:
            info = [int(i) + FRAMES_ADD - 1 for i in re.match(r'\[(?P<value>\s+\d+\s+\d+)\]',i).group('value').split()]

        except:
            info = [int(i) + FRAMES_ADD - 1 for i in re.match(r'\[(?P<value>\d+\s+\d+)\]', i).group('value').split()]

        # print(info)
        # os.system("pause")

        info_list_1 = [re.search(r'\s+\[(?P<value>.*)\]', i).group('value'), info]

        # print(info_list_1)
        # os.system("pause")

        info_list.append(info_list_1)
        # print(i)

    # print(info_list)
    return info_list
    #最后的效果:[['', [0, 18]], ['お', [19, 24]], ['願い', [25, 49]], ['三', [50, 82]], ['。', [83, 86]]]

    #[  37   58]  0.562999  で+接続詞	[で]





