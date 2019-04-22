import csv,sys
import os


def chawenjianla():
    pici = r'C:\Users\a7825\Desktop\工作空间\语音数据\RWCP-SP96-要切\第一批 - 副本 (2)'
    #批次的目录

    keka = 'keka'
    #识别结果

    wav = 'wav'
    #波形文件

    shan_1_out = []
    shan_1_wav = []
    shan_2_out = []
    shan_2_wav = []
    #把需要删掉的文件的路径先保存下来


    for a in os.listdir(pici):

        pici_2 = os.path.join(pici,a,keka)
        pici_4 = os.path.join(pici,a,wav)

        kekafile = os.listdir(pici_2)
        wavefile = os.listdir(pici_4)

        if len(kekafile) != len(wavefile):
            print("%s 这个文件夹下.out文件和wave文件的数量不一样"%a)

        for x in kekafile:

            pici_3 = os.path.join(pici_2,x)

            txtwenjian = csv.reader(open(pici_3, 'r', encoding='utf-8'))
            b = [i for i in txtwenjian]
            if len(b) == 0:
                print(x)

                path_shan_1_out = os.path.join(pici_2,x)
                shan_1_out.append(path_shan_1_out)

                path_shan_1_wav = os.path.join(pici_4,x.replace('.out','.wav'))
                shan_1_wav.append(path_shan_1_wav)
                #发现.out文件中有空文件就把对应的wav文件还有.out文件删了


            for i in b:
                # print(i)
                # os.system('pause')
                if i[0] == 'sentence1:  。' or i[0] == '<input rejected by short input>':
                    print(x)

                    path_shan_2_out = os.path.join(pici_2,x)
                    shan_2_out.append(path_shan_2_out)

                    path_shan_2_wav = os.path.join(pici_4,x.replace('.out','.wav'))
                    shan_2_wav.append(path_shan_2_wav)
                    #发现.out文件中出现以上语句，就把对应的wav文件删了，还有对应的.out文件也删了

    for path_fi in shan_1_out:
        try:
            os.remove(path_fi)
        except:
            continue

    for path_fi in shan_1_wav:
        try:
            os.remove(path_fi)
        except:
            continue

    for path_fi in shan_2_out:
        try:
            os.remove(path_fi)
        except:
            continue

    for path_fi in shan_2_wav:
        try:
            os.remove(path_fi)
        except:
            continue



