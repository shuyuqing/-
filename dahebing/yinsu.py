import os
import pipei_yinsu as pei

def yinsu(zhengjie,start_1,end_1,ID_1,path):

    shouzimu = zhengjie[0]
    weizimu =zhengjie[-1]

    start_2 = 0
    end_2 = 0

    path_out = os.path.join(path, 'keka_yinsu', ID_1 + '.out')

    dianout_yinsu = pei.read_out(path_out)

    for i in dianout_yinsu:

        if shouzimu in i[0] and start_1<=i[1][0]<=end_1: #当shouzimu in i[0] shouzimu = [0]同时发生时，优先选择shouzimu = [0]

            if start_2 == 0:

                start_2 = i[1][0]

            if shouzimu == i[0]:

                start_2 = i[1][0]

        if weizimu in i[0] and start_1<=i[1][1]<=end_1:

            if end_2 == 0:
                end_2 = i[1][1]

            if weizimu == i[0]:
                end_2 = i[1][1]

    print('首字母:%s'%shouzimu)
    print('尾字母:%s'%weizimu)

    print("音素的结束帧数是")
    print(end_2)
    print("音素的开始帧数是")
    print(start_2)

    # if start_2 == 0 and end_2 == 0:
    #
    #     print("因音素上找不到对应")
    #     print("文件ID为%s"%ID_1)
    #     os.system('pause')

    return start_2,end_2