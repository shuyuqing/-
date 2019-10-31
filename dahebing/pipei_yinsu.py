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
    # i = re.findall(r'\[.*', text)
    # print(i)
    # os.system('pause')
    # for i in re.findall(r'\[.*\]', text):
    bianhao = re.findall(r'\[.*', text)

    bianhao.pop(0)
    bianhao.pop(-1)

    for i in bianhao:

        #这里的话\就相当于/，在[的前面加上\就相当于我要匹配"["
        #这里的.匹配除了换行符之外的所有东西
        #*是重复的意思，例如，ca*t 将匹配 'ct' (0个 'a' 字符)，'cat' (1个``'a')，` `'caaat' (3个 'a' 字符)，等等。
        #findall返回的是一个列表
        #split()会返回分割后的字符串列表。

        #"+的"意思是大于等于一个
        #(?P<value>\s+\d+\s+\d+),这里使用了捕获组来获取[]里面的值

        try:#把音素对应的帧的编号范围匹配出来
            info = [int(i) + FRAMES_ADD - 1 for i in re.match(r'\[(?P<value>\s+\d+\s+\d+)\]',i).group('value').split()]
            #match只匹配开头部分,函数group()可以返回被匹配到的字符串
        except:
            info = [int(i) + FRAMES_ADD - 1 for i in re.match(r'\[(?P<value>\d+\s+\d+)\]', i).group('value').split()]

        # print(info)

        # info_list_0 = re.search(r'\s+(?P<value>\w+)\_\w+\-(?P<value1>\w+)\_\w+\+(?P<value2>\w+)\_\w+',i)

        # print(i)

        if i[-1] ==']':#[   3    8]  1.222721  sp_S-sh_B+i_I[sp-sh_B+i:_B]把这种样子的字符串后面的中括号去掉

            a = i.replace(re.findall(r'\[\S+\_\S+\]', i)[0], '')
            i = a

        # print(i)

        info_list_0 = re.search(r'\s+(?P<value>\S+)\_\w+\-(?P<value1>\S+)\_\w+\+(?P<value2>\S+)\_\w+',i)

        # diyige = info_list_0.group('value')
        # print(file_path)
        # print(info_list_0.group())
        # os.system('pause')


        dierge = info_list_0.group('value1')#判定该音素在哪个范围要看.out文件中中间的那个音素

        # if dierge == "N":
        #     dierge = 'n'
        if dierge == 'sp':
            dierge = '、'
        # if dierge[-1] == ':':
        #
        #     if dierge[0] == 'o':
        #         dierge = 'ou'
        #     else:
        #         dierge_1 = dierge[0]+dierge[0]
        #         dierge = dierge_1
        #之前没有用julius工具的时候，用来变换音素用的

        # disange = info_list_0.group('value2')

        # print(i)
        # print(info_list_0.group('value'))
        # print(info_list_0.group('value1'))
        # print(info_list_0.group('value2'))

        # os.system("pause")

        info_list_1 = [dierge, info]
        #这里使用捕获组来获取了[]里面的文字

        # print(info_list_1)
        # os.system("pause")

        info_list.append(info_list_1)
        # print(i)

        info_list_1 = info_list.copy()#这里只能用浅度拷贝不能直接复制
        n = 0
        for item in info_list_1:#把逗号pop掉

            if item[0] == '、':
                info_list.pop(n)
                n = n -1

            n+=1


    # print(info_list)
    # os.system('pause')
    return info_list

    #[  37   58]  0.562999  で+接続詞	[で]



# read_out(file_path = r'C:\Users\a7825\Desktop\C001L/C001L_007_1.out')