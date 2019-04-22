#用于从chasen出力文件中取出已经分割好了的单词，然后把句子写入新的txt文件中
#首先我得通过认识结果把需要的正解文从.txt文件中取出来，写入到另外一个.txt文件中去
#之后就会得到.ref文件，然后去dianlog.py文本中操作
#记住，必须要重新在linux中新建一个.ref文件，把在windows上生成的,ref文件的内容复制到这个新建的文件中去，才能被scoring识别
import csv
import os
import dianlog_RWCP_SP96 as di

def qu(path_1):

    path = path_1
    for mulu in os.listdir(path):

        jushiqi = 0
        file_dir = os.path.join(path,mulu)
        #chasen的出力文件的地址以及整理之后的文件的地址

        file_dir_2 = os.path.join(file_dir,'keka')
        #原本的.out文件的路劲，仅仅是想要把文件名取出来

        feature = 'chasen.txt'
        feature_1 = 'chasen.ref'

        files_dir = os.path.join(file_dir,feature)
        t = open(files_dir, 'r',encoding='utf-8')#要不要加上 encoding='utf-8'，视具体情况而定
        txtwenjian = csv.reader(t)
        data = [i for i in txtwenjian]#一列一列地取出来装进list里面去
        data_1 = []
        n = 0
        banyun = ''
        banyun_1 = []
        banyun_2 = []

        for a in data:
            a[0] = (a[0].split())[0]#只把第一列的所有单词取出来,这里其实已经把data里面的内容改变了
            # [['うんお願いします。'], ['うん'], ['お願い'], ['し'], ['ます'], ['。'], ['EOS'], ['うん。'], ['うん'], ['。'], ['EOS']]

        for i in data:

            if i[0] == '。':

                banyun_1.append(i[0])

            elif i[0]=='EOS':#发现EOS就删除这个列表开头的第一个元素
                banyun_1.pop(0)
                jushiqi = jushiqi +1

                banyun_2.append(banyun_1)
                banyun_1 = []

            else:
                banyun_1.append(i[0]+' ')
        # print(banyun_2)

        for t in banyun_2:
            data_1.append(''.join(t)) #把list里面的元素全部都合并了
        # print(data_1)

        files_dir_1 = os.path.join(file_dir, feature_1)

        with open(files_dir_1, 'w',encoding='utf-8') as f:#把正解文一句一句地写入新的txt文件
            name = os.listdir(file_dir_2)

            #以下是RWCP_SP96专用的代码
            name.sort(key=lambda ele: int(ele.split('_')[1]))  # 把每个元素都用split函数拆开，以第二个字符串的大小为基准，进行排序
            name.sort(key=lambda ele: ele.split('_')[0])  # 然后再以拆开的第一个字符串为基准进行排序

            if jushiqi != len(name):
                print("请注意，正解文的数量跟.out文件的数量不一样")
                print(mulu)

            #注意，这部分是RWCP专用
            # name.sort(key=lambda ele: int(ele.split('_')[1]))  # 把每个元素都用split函数拆开，以第二个字符串的大小为基准，进行排序
            # name.sort(key=lambda ele: ele.split('_')[0])  # 然后再以拆开的第一个字符串为基准进行排序

            n = 0
            for u in data_1:
                    # print("data_1的大小为")
                    # print(len(data_1))
                    # print("n的值为%d"%n)
                    # os.system("pause")
                    f.writelines(name[n].replace(".out",'') + '\n')#记住，删除字符串中的某一段用replace
                    f.writelines(u+'\n')#每写一句就空一行
                    n=n+1

            f.writelines(name[n - 1].replace(".out", '') + '\n')  # 为了能够让生成的标志文件的结尾不会出现实心圆点，故意把最后一句话重复写了一遍
            f.writelines(data_1[-1] + '\n')

    di.logwen(path)