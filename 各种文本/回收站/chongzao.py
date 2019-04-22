import os

def chongzao(l_biaozhi,l_jieguo_1,dianout_2,ID):#四个参数分别是标志list/scoring之后的识别结果/通过.out文件解析出来的list/文件ID

    dianout_1 = []#生成的新的.out解析出来的list

    jishuqi_l_jieguo_1 = 0#l_biaozhi跟l_jieguo_1是一一对应的，所以这两个list共用一个计数器
    jishuqi_dianout = 0

    # print(dianout)
    # os.system('pause')
    # 最后的效果:[['お', [19, 24]], ['願い', [25, 49]], ['三', [50, 82]], ['。', [83, 86]]]
    for i in dianout_2:

        danci_dianout = i[0]#原版的.out文件解析出来的list
        danci_l_jieguo_1 = l_jieguo_1[jishuqi_l_jieguo_1]#经过socring工具之后的align文件中的识别结果的单词

        while danci_l_jieguo_1 == '':#由于经过socring工具之后的align文件中的识别结果是有空字符存在的，所以遇到空字符就跳过

            jishuqi_l_jieguo_1 += 1
            danci_l_jieguo_1 = l_jieguo_1[jishuqi_l_jieguo_1]

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

        if danci_dianout == danci_l_jieguo_1:

            i.append(l_biaozhi[jishuqi_l_jieguo_1])
            dianout_1.append(i)#往新构建的list中加入元来dianout中的单词

        else:#这里默认.out文件的单词被scoring工具合并了，所以它应该比输出文件的识别结果的单词短

            danci_dianout_1 = i[0] + dianout_2[jishuqi_dianout+1][0]

            if danci_dianout_1 == danci_l_jieguo_1:

                i[0] = danci_dianout_1#把两个单词拼接起来
                i[1][1] = dianout_2[jishuqi_dianout+1][1][1]
                i.append(l_biaozhi[jishuqi_l_jieguo_1])#一旦对dianout_2里面的元素进行过操作，那么就会改变函数之外的变量
                dianout_1.append(i)

                jishuqi_dianout += 1#因为用dianout的list中的两个单词拼接成一个单词之后发现对上了，所以计数器要加一，最后再加1，下次才能跳到想要比较的单词那里

            else:#不行就拼三个单词

                danci_dianout_1 = i[0] + dianout_2[jishuqi_dianout+1][0] + dianout_2[jishuqi_dianout+2][0]

                if danci_dianout_1 == danci_l_jieguo_1:
                    i[0] = danci_dianout_1  # 把两个单词拼接起来
                    i[1][1] = dianout_2[jishuqi_dianout + 2][1][1]
                    i.append('C')
                    dianout_1.append(i)

                    jishuqi_dianout += 2#因为用dianout的list中的三个单词拼接成一个单词之后发现对上了，所以计数器要加二，最后再加1，下次才能跳到想要比较的单词那里


                else:
                    print(ID)
                    print('拼了三次都没有成功')
                    os.system('pause')

        jishuqi_l_jieguo_1 += 1
        jishuqi_dianout += 1

    return dianout_1