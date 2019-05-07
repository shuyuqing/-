##用于第二版打标签的文本，用于处理特征值的行数小于识别结果的最后一帧的编号的情况
def biaoqian(out_list_1, item_1, t_file_list_1, index_1):
    start = out_list_1[index_1][1][0]
    end =len(t_file_list_1)
    # 移除被分割开的单词的前后的空格(来自正解文)
    a = item_1.strip()
    # 识别结果中分割开的单词(来自识别结果)
    b = out_list_1[index_1][0].strip()
    if a == b:
        # 对比成功
        # print('[+]对比成功:%s-----%s' % (a, b))
    # 根据帧数去正解文件中打标签
        for i in range(start-1, end):
            t_file_list_1[i].insert(0, '0')
    else:
        # print('[-]对比失败:%s-----%s' % (a, b))
        # 对比失败
        for i in range(start-1, end):
            t_file_list_1[i].insert(0, '1')

    return t_file_list_1