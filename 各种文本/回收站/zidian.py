def zidian(dir, BASE_DIRS):  # 建立三个字典

    import csv,os
    name1 = 'align1'
    name2 = 'align1.txt'
    shibiejieguo = {}
    # 安放识别结果的字典

    symbolcidian = {}
    # 这样的词典,标志词典

    zhengjie = {}
    # 正解文词典

    txtwenjian = csv.reader(open(os.path.join(BASE_DIRS, dir, name1), 'r', encoding='EUC-JP'))  # 把symbol标志文件读进来,编码有问题的话就用encoding='utf-8'

    # txtwenjian = csv.reader(open(os.path.join(BASE_DIRS, dir, name2), 'r', encoding='utf-8'))

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
                symbolcidian[banyun.replace('id: ', '')] = s  # symbolcidian[C001L_016] = [C,S,C,C,S,S,D]

            if 'REF' in q[0]:
                s = q[0].split()
                s.pop(0)
                # print(len(s))
                # print(s)
                zhengjie[banyun.replace('id: ', '')] = s  # zhengjie[C001L_016] = [ま,男,の,人,が,い,て,。]

        else:
            pass

    return zhengjie, symbolcidian