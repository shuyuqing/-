import os
import re
FRAMES_ADD = 1

def read_out(info_list,file_path):

    text_file = open(file_path, 'r', encoding='utf-8')
    text = text_file.read()#read()读全部,readline()读一行,readlines()读所有行

    xinlai = re.findall(r'cmscore1:.*',text)#把信赖度哪一行匹配出来

    # print(xinlai)

    xinlai_1 = xinlai[0].split()#把列表里的各个部分split开

    xinlai_1.pop(0)#把第一个值pop掉

    # print(xinlai_1)

    xinlai_1.pop(0)

    # print(xinlai_1)

    xinlai_1.pop(-1)

    # print(xinlai_1)

    n = 0#xinlai_1的下标

    info_list_2 = []

    for yu in info_list:

        if yu[0] != '' and yu[0] != '。':

            yu.append(xinlai_1[n])

            n+=1

            info_list_2.append(yu)

    # print(info_list_2)

    # os.system('pause')

    return info_list_2
    #最后的效果:[['', [0, 18]], ['お', [19, 24]], ['願い', [25, 49]], ['三', [50, 82]], ['。', [83, 86]]]

    #[  37   58]  0.562999  で+接続詞	[で]



# read_out(file_path = r'C:\Users\a7825\Desktop\工作空间\杂物\对比\symbol\C001L\keka/C001L_089.out')

