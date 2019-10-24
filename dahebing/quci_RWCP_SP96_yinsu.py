#用于从chasen出力文件中取出已经分割好了的单词，然后把句子写入新的txt文件中
#首先我得通过认识结果把需要的正解文从.txt文件中取出来，写入到另外一个.txt文件中去
#之后就会得到.ref文件，然后去dianlog.py文本中操作
#记住，必须要重新在linux中新建一个.ref文件，把在windows上生成的,ref文件的内容复制到这个新建的文件中去，才能被scoring识别
import csv
import os

def qu(path_1):#生成正解文的函数

    path = path_1
    for mulu in os.listdir(path):

        jushiqi = 0
        file_dir = os.path.join(path,mulu)
        #chasen的出力文件的地址以及整理之后的文件的地址

        file_dir_2 = os.path.join(file_dir,'keka')
        #原本的.out文件的路劲，仅仅是想要把文件名取出来

        feature = 'zhuan_'+mulu+'_chasen_1.txt'
        feature_1 = 'chasen_1.ref'

        files_dir = os.path.join(file_dir,feature)
        t = open(files_dir, 'r',encoding='utf-8')#要不要加上 encoding='utf-8'，视具体情况而定
        txtwenjian = csv.reader(t)
        data = [i for i in txtwenjian]#一列一列地取出来装进list里面去
        data_1 = []
        data_2 = []
        data_3 = []
        n = 0
        banyun_1 = []
        banyun_2 = []

        for a in data:

            data_1.append(a[0].split())
            # banyun_1.append(a[0].split())
            # data_1.append(banyun_1)
            # banyun_1 = []

        for ci in data_1:

            if len(ci)!=1:
                ci.pop(0)
                banyun_1.append(' '.join(ci))
                data_2.append(banyun_1)
                banyun_1 = []

            if ci[0] == 'EOS':
                banyun_1.append(ci[0])
                data_2.append(banyun_1)
                banyun_1=[]

        data_3 = []
        banyun = ''
        for yu in data_2:
            if yu[0] != 'EOS':
                if banyun == '':
                    banyun = yu[0]
                else:
                    banyun = banyun + ' ' + yu[0]
            else:
                data_3.append(banyun)
                banyun = ''

        for t in banyun_2:
            data_1.append(''.join(t)) #把list里面的元素全部都合并了
        # print(data_1)

        files_dir_1 = os.path.join(file_dir, feature_1)

        with open(files_dir_1, 'w',encoding='utf-8') as f:#把正解文一句一句地写入新的txt文件
            name = os.listdir(file_dir_2)

            #以下是RWCP_SP96专用的代码
            # name.sort(key=lambda ele: int(ele.split('_')[1]))  # 把每个元素都用split函数拆开，以第二个字符串的大小为基准，进行排序
            # name.sort(key=lambda ele: ele.split('_')[0])  # 然后再以拆开的第一个字符串为基准进行排序

            if len(data_3) != len(name):
                print("请注意，正解文的数量跟.out文件的数量不一样")
                print(mulu)

            #注意，这部分是RWCP专用
            # name.sort(key=lambda ele: int(ele.split('_')[1]))  # 把每个元素都用split函数拆开，以第二个字符串的大小为基准，进行排序
            # name.sort(key=lambda ele: ele.split('_')[0])  # 然后再以拆开的第一个字符串为基准进行排序

            n = 0#keka文件的序号
            for u in data_3:
                    # print("data_1的大小为")
                    # print(len(data_1))
                    # print("n的值为%d"%n)
                    # os.system("pause")
                    f.writelines(name[n].replace(".out",'') + '\n')#记住，删除字符串中的某一段用replace
                    f.writelines(u+'\n')#每写一句就空一行
                    n=n+1

            f.writelines(name[n - 1].replace(".out", '') + '\n')  # 为了能够让生成的标志文件的结尾不会出现实心圆点，故意把最后一句话重复写了一遍
            f.writelines(data_3[-1])


# 根据原有的.out文件生成能被scoring所识别的标准日志文件
# 把日志文件跟.ref文件一起输入scoring工具，就能获得带CCCCCSSSSS标志的文件了
# 记住，必须要重新在linux中新建一个.ref文件，把在windows上生成的,ref文件的内容复制到这个新建的文件中去，才能被scoring识别
import csv
import os
import pipei_yinsu
def logwen(path):#生成识别结果的函数

    for mulu in os.listdir(path):

        basedir = os.path.join(path, mulu)

        file_dir = os.path.join(basedir, 'keka_yinsu')
        # 原始的.out文件摆放的位置

        wenjianid = "Stat: adin_file: input speechfile: "
        # 加入到out文件的第一句话

        file_dir_1 = basedir
        # 生成新的log文件的存放地址

        banyun = []
        files_dir_1 = os.path.join(file_dir_1, "chasen_1.log")

        file_dir_list = os.listdir(file_dir)

        # 注意，这部分是RWCP专用
        # file_dir_list.sort(key=lambda ele: int(ele.split('_')[1]))  # 把每个元素都用split函数拆开，以第二个字符串的大小为基准，进行排序
        # file_dir_list.sort(key=lambda ele: ele.split('_')[0])  # 然后再以拆开的第一个字符串为基准进行排序

        with open(files_dir_1, 'w', encoding='utf-8') as f:  # 把正解文一句一句地写入新的log文件

            for i in file_dir_list:#每次看一个.out文件
                files_dir = os.path.join(file_dir, i)
                data = pipei_yinsu.read_out(files_dir)

                # print(data)
                yinsu_1 = ''
                for yinsu in data:#把音素一个接一个扔到list里面去
                    if yinsu[0]!='、':
                        yinsu_1 = yinsu_1 + yinsu[0] + ' '

                f.writelines(wenjianid + i.replace(".out", ".wav") + '\n')
                f.writelines('sentence1:  '+yinsu_1+ '\n')

            f.writelines(wenjianid + file_dir_list[-1].replace(".out", ".wav") + '\n')
            f.writelines('sentence1:  '+data[-1][0])

logwen(path=r'C:\Users\a7825\Desktop\新建文件夹\新建文件夹')