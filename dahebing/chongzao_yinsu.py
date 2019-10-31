import os
import copy
# import pykakasi #把平假名或片假名转化为读音
# import make_kana_convertor
# import strQ2B


def chongzao(l_biaozhi,l_jieguo_1,dianout_2,ID,l_zhengjie_1):#四个参数分别是标志list/scoring之后的识别结果/通过.out文件解析出来的list/文件ID


    dianout_1 = []#生成的新的.out解析出来的list

    jishuqi_l_jieguo_1 = 0#l_biaozhi跟l_jieguo_1是一一对应的，所以这两个list共用一个计数器
    jishuqi_dianout = 0
    jishuqi_zhengjie = 0

    dianout_3 = copy.deepcopy(dianout_2)#为了不改变函数外面的dianout的值

    # print(dianout)
    # os.system('pause')
    # 最后的效果:[['お', [19, 24]], ['願い', [25, 49]], ['三', [50, 82]], ['。', [83, 86]]]
    for i in l_jieguo_1:

        if i != '':

            danci_dianout = dianout_3[jishuqi_dianout][0]#原版的.out文件解析出来的list
            danci_l_jieguo_1 = l_jieguo_1[jishuqi_l_jieguo_1]#经过socring工具之后的align文件中的识别结果的单词

            if len(danci_l_jieguo_1) < len(danci_dianout):

                print(ID)
                print("这个文件的.out里的单词居然比识别结果的单词长")
                print("danci_l_jieguo_1")
                print(danci_l_jieguo_1)
                print("danci_dianout")
                print(danci_dianout)
                print("dianout_1")
                print(dianout_1)
                os.system('pause')

            # if conv.do(danci_dianout) == danci_dianout and danci_dianout != '、':  # 判断是不是字母
            #
            #     try:
            #         danci_dianout = conv.do(make_kana_convertor._make_kana_convertor(strQ2B.strQ2B(danci_dianout)))
            #
            #     except:
            #         danci_dianout = conv.do(make_kana_convertor._make_kana_convertor(danci_dianout))

            if danci_dianout == danci_l_jieguo_1:

                dianout_3[jishuqi_dianout].append(l_biaozhi[jishuqi_l_jieguo_1])
                dianout_1.append(dianout_3[jishuqi_dianout])

                if l_biaozhi[jishuqi_l_jieguo_1] == 'S':  # 如果标志是S，就把这个单词对应的正解加入进的list，之后转化了看看是不是和识别结果一样

                    dianout_3[jishuqi_dianout].append(l_zhengjie_1[jishuqi_zhengjie])

                if l_biaozhi[jishuqi_l_jieguo_1] == 'I':  # 如果标志是I,就把这个单词对应的前一个和后一个单词加入list中去

                    try:
                        dianout_3[jishuqi_dianout].append(l_zhengjie_1[jishuqi_zhengjie - 1])
                    except:
                        pass

                    try:
                        dianout_3[jishuqi_dianout].append(l_zhengjie_1[jishuqi_zhengjie + 1])
                    except:
                        pass

            else:#这里默认.out文件的单词被scoring工具合并了，所以它应该比输出文件的识别结果的单词短

                danci_dianout_1 = dianout_3[jishuqi_dianout][0] + dianout_2[jishuqi_dianout+1][0]

                if danci_dianout_1 == danci_l_jieguo_1:

                    dianout_3[jishuqi_dianout][0] = danci_dianout_1#把两个单词拼接起来
                    dianout_3[jishuqi_dianout][1][1] = dianout_2[jishuqi_dianout+1][1][1]
                    dianout_3[jishuqi_dianout].append(l_biaozhi[jishuqi_l_jieguo_1])
                    dianout_1.append(dianout_3[jishuqi_dianout])

                    if l_biaozhi[jishuqi_l_jieguo_1] == 'S':  # 如果标志是S，就把这个单词对应的正解加入进的list

                        dianout_3[jishuqi_dianout].append(l_zhengjie_1[jishuqi_zhengjie])

                    if l_biaozhi[jishuqi_l_jieguo_1] == 'I':  # 如果标志是I,就把这个单词对应的前一个和后一个单词加入list中去

                        try:
                            dianout_3[jishuqi_dianout].append(l_zhengjie_1[jishuqi_zhengjie - 1])
                        except:
                            pass

                        try:
                            dianout_3[jishuqi_dianout].append(l_zhengjie_1[jishuqi_zhengjie + 1])
                        except:
                            pass

                    jishuqi_dianout += 1#因为用dianout的list中的两个单词拼接成一个单词之后发现对上了，所以计数器要加一，最后再加1，下次才能跳到想要比较的单词那里

                else:#不行就拼三个单词

                    danci_dianout_1 = dianout_3[jishuqi_dianout][0] + dianout_2[jishuqi_dianout+1][0] + dianout_2[jishuqi_dianout+2][0]

                    if danci_dianout_1 == danci_l_jieguo_1:
                        dianout_3[jishuqi_dianout][0] = danci_dianout_1  # 把两个单词拼接起来
                        dianout_3[jishuqi_dianout][1][1] = dianout_2[jishuqi_dianout + 2][1][1]
                        dianout_3[jishuqi_dianout].append(l_biaozhi[jishuqi_l_jieguo_1])
                        dianout_1.append(dianout_3[jishuqi_dianout])

                        if l_biaozhi[jishuqi_l_jieguo_1] == 'S':  # 如果标志是S，就把这个单词对应的正解加入进的list

                            dianout_3[jishuqi_dianout].append(l_zhengjie_1[jishuqi_zhengjie])

                        if l_biaozhi[jishuqi_l_jieguo_1] == 'I':  # 如果标志是I,就把这个单词对应的前一个和后一个单词加入list中去

                            try:
                                dianout_3[jishuqi_dianout].append(l_zhengjie_1[jishuqi_zhengjie - 1])
                            except:
                                pass

                            try:
                                dianout_3[jishuqi_dianout].append(l_zhengjie_1[jishuqi_zhengjie + 1])
                            except:
                                pass

                        jishuqi_dianout += 2#因为用dianout的list中的三个单词拼接成一个单词之后发现对上了，所以计数器要加二，最后再加1，下次才能跳到想要比较的单词那里

                    else:

                        danci_dianout_1 = dianout_3[jishuqi_dianout][0] + dianout_2[jishuqi_dianout + 1][0] + dianout_2[jishuqi_dianout + 2][0] + dianout_2[jishuqi_dianout + 3][0]

                        if danci_dianout_1 == danci_l_jieguo_1:
                            dianout_3[jishuqi_dianout][0] = danci_dianout_1  # 把两个单词拼接起来
                            dianout_3[jishuqi_dianout][1][1] = dianout_2[jishuqi_dianout + 3][1][1]
                            dianout_3[jishuqi_dianout].append(l_biaozhi[jishuqi_l_jieguo_1])
                            dianout_1.append(dianout_3[jishuqi_dianout])

                            if l_biaozhi[jishuqi_l_jieguo_1] == 'S':  # 如果标志是S，就把这个单词对应的正解加入进的list

                                dianout_3[jishuqi_dianout].append(l_zhengjie_1[jishuqi_zhengjie])

                            if l_biaozhi[jishuqi_l_jieguo_1] == 'I':  # 如果标志是I,就把这个单词对应的前一个和后一个单词加入list中去

                                try:
                                    dianout_3[jishuqi_dianout].append(l_zhengjie_1[jishuqi_zhengjie - 1])
                                except:
                                    pass

                                try:
                                    dianout_3[jishuqi_dianout].append(l_zhengjie_1[jishuqi_zhengjie + 1])
                                except:
                                    pass

                            jishuqi_dianout += 3  # 因为用dianout的list中的四个单词拼接成一个单词之后发现对上了，所以计数器要加3，最后再加1，下次才能跳到想要比较的单词那里

                        else:
                            print("danci_dianout_1")
                            print(danci_dianout_1)
                            print("danci_l_jieguo_1")
                            print(danci_l_jieguo_1)

                            print(ID)
                            print('拼了四次都没有成功')

                            os.system('pause')


            jishuqi_l_jieguo_1 += 1
            jishuqi_dianout += 1
            jishuqi_zhengjie += 1

        else:

            jishuqi_l_jieguo_1 += 1
            jishuqi_zhengjie += 1

    return dianout_1