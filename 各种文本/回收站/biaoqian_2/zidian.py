def zidian(path):  # 建立三个字典

    import csv,os
    name1 = 'align1'
    name2 = 'align1.txt'

    l_jieguo = []
    # 安放识别结果的字典

    l_biaozhi_1 = []
    # 这样的词典,标志词典

    l_zhengjie_1 = []
    # 正解文词典

    # txtwenjian = csv.reader(open(os.path.join(path, name2), 'r', encoding='utf-8'))

    for q in biaozhiwenjian:
        if q != []:
            if 'id' in q[0]:
                ID = q[0].replace('id: ', '')  # 标志文件里面有文件名
                # print(q[0])  # 这里的id就是文件名

            if 'EVAL' in q[0]:
                s = q[0].split()
                s.pop(0)  # 把列表的第一个元素pop掉

                # while 'I' in s:
                #     s.remove('I')  # 一次性只会删除一个I,所以要用while,很多时候是因为I，符号的个数比正解文的单词数还要多
                # # print(len(s))
                # # os.system("pause")
                # symbolcidian[banyun.replace('id: ', '')] = s  # symbolcidian[C001L_016] = [C,S,C,C,S,S,D]

                l_biaozhi = s

            if 'REF' in q[0]:
                s = q[0].split()
                s.pop(0)
                # print(len(s))
                # print(s)
                l_zhengjie = s

        else:
            pass

    for y in range(len(l_biaozhi)):

        if l_biaozhi[y] == 'D':
            l_zhengjie_1.append(l_zhengjie)

    return zhengjie, symbo