#用于第三版打标签的文本，用于把识别结果中句号的部分的特征值全部打上标签9，之后再把被标记过数字9的特征值删除掉，
# 用于处理最后特征值行数没有识别结果的最后一帧的编号大的情况

def biaoqian(out_list_1, item_1, t_file_list_1, index_1):
    start = out_list_1[index_1][1][0]
    end =len(t_file_list_1)
    # 移除被分割开的单词的前后的空格(来自正解文)
    a = item_1.strip()
    # 识别结果中分割开的单词(来自识别结果)
    b = out_list_1[index_1][0].strip()
    # if a == b:
    #     # 对比成功
    #     # print('[+]对比成功:%s-----%s' % (a, b))
    # # 根据帧数去正解文件中打标签
    #     for i in range(start-1, end):
    #         t_file_list_1[i].insert(0, '0')
    # else:
    #     # print('[-]对比失败:%s-----%s' % (a, b))
    #     # 对比失败
    #     for i in range(start-1, end):
    #         t_file_list_1[i].insert(0, '1')

    if a == '。':  # 如果对比到了最后的句号，就插入数字9，之后再把被标记过数字9的特征值删除掉
        for i in range(start - 1, end):
            t_file_list_1[i].insert(0, '9')

    elif a == b:
        # 对比成功
        # print('[+]对比成功:%s-----%s' % (a, b))
        # 根据帧数去正解文件中打标签
        for i in range(start - 1, end):
            t_file_list_1[i].insert(0, '0')

    elif a != b:
        for i in range(start - 1, end):
            t_file_list_1[i].insert(0, '1')

    return t_file_list_1