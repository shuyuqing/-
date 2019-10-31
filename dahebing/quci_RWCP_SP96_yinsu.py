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

        file_dir_2 = os.path.join(file_dir,'keka_yinsu')
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
                print(mulu)
                print("请注意，正解文的数量跟.out文件的数量不一样")
                print('.out文件的数量为')
                print(len(name))
                print('正解文的数量为')
                print(len(data_3))
                print(data_3)
                print(name)


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

            # f.writelines(name[n - 1].replace(".out", '') + '\n')  # 为了能够让生成的标志文件的结尾不会出现实心圆点，故意把最后一句话重复写了一遍
            # f.writelines(data_3[-1])


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

                # you = False#检查识别结果中有没有冒号
                # for danci in data:#如果识别结果中出现冒号“：”就把单词单位的识别结果读出来看看到底是“u”还是“-”
                #     if ':' in danci[0]:
                #         you = True
                # if you == True:
                _data = changpoyin(data, files_dir, i)  # 改造之后的新的列表,

                # print(data)
                # print(_data)
                # os.system('pause')

                yinsu_1 = ''
                for yinsu in _data:#把音素一个接一个扔到list里面去
                    if yinsu[0]!='、':
                        yinsu_1 = yinsu_1 + yinsu[0] + ' '

                f.writelines(wenjianid + i.replace(".out", ".wav") + '\n')
                f.writelines('sentence1:  '+yinsu_1+ '\n')

#从chasen文件中把正解文的読み拿出来，准备给音素转化工具使用(C064L_chasen_1.txt)
import csv
import os
import jaconv#把片假名转化为平假名

def pinjia(path_1):

    path = path_1
    for mulu in os.listdir(path):#每一个循环读到一个大文件C064L，C064R

        jushiqi = 0
        file_dir = os.path.join(path,mulu)
        #chasen的出力文件的地址以及整理之后的文件的地址

        file_dir_2 = os.path.join(file_dir,'keka')
        #原本的.out文件的路劲，仅仅是想要把文件名取出来

        feature = 'chasen.txt'
        feature_1 = 'chasen.ref'
        feature_2 = mulu +'_'+'chasen_1.txt'

        files_dir = os.path.join(file_dir,feature)

        save_dir = os.path.join(file_dir,feature_2)

        with open(files_dir,  'r',encoding='utf-8') as csvfile:

            reader = csv.reader(csvfile)

            column = [row for row in reader]

            column_2 = []

            for xiang in column:
                column_2.append(xiang[0].split())

            column_1 = []
            banyun = []

            for xiang in column_2:

                if len(xiang) == 1:

                    banyun.append(xiang[0])
                    column_1.append(banyun)
                    banyun = []

                else:
                    if xiang[0] != '、' and xiang[0] != '。':
                        if xiang[1] == '未知語':
                            banyun.append(xiang[0] + ' ' + jaconv.kata2hira(xiang[0]))
                        else:
                            banyun.append(xiang[0] + ' ' + jaconv.kata2hira(xiang[1]))
                        column_1.append(banyun)
                        banyun = []

            print(column_1)

            with open(save_dir, 'w', encoding='utf-8') as f:  # 把正解文一句一句地写入新的txt文件
                for xieru in column_1:
                    f.writelines(xieru[0] + '\n')


import pipei
import make_kana_convertor as ztok#把字母转化成读音
import copy
def changpoyin(data,files_dir,i):#把长破音都转化为u,这里的i是文件的id

    from pykakasi import kakasi  # 把单词转化为音素
    kakasi = kakasi()
    kakasi.setMode("H", "a")  # Hiragana to ascii, default: no conversion
    kakasi.setMode("K", "a")  # Katakana to ascii, default: no conversion
    kakasi.setMode("J", "a")  # Japanese to ascii, default: no conversion
    kakasi.setMode("r", "Hepburn")  # default: use Hepburn Roman table
    kakasi.setMode("s", True)  # add space, default: no separator
    conv = kakasi.getConverter()

    data_1 = copy.deepcopy(data)
    data_2 = []

    files_dir_1 = os.path.join(files_dir.replace('_yinsu', ''))
    data_danci = pipei.read_out(files_dir_1)  # 单词级别的识别结果

    for danci in data_1:#每次循环检查一个音素(音素単位)

        if ':' in danci[0]:#如果识别结果中出现冒号“：”就把单词单位的识别结果读出来看看到底是“u”还是“-”

            zhenshu = danci[1][0]

            for danci_1 in data_danci:#每一个循环查看一个单词(単語単位)

                if zhenshu >= danci_1[1][0] and zhenshu <= danci_1[1][1]:  # 找到这个音素对应的汉字

                    print('能找到')

                    tanngou = conv.do(danci_1[0])  # 把这个汉字取出进行转化

                    if danci_1[0] == tanngou:  # 说明是字母

                        tanngou = ztok._make_kana_convertor(danci_1[0])

                    if tanngou[-1] == 'u':#如果结尾是u那就把识别结果里的:转化为u

                        fenjie = (danci[1][0] + danci[1][1])//2
                        danci_2 = copy.deepcopy(danci)
                        danci_2[1][1] = fenjie
                        danci_2[0] = danci_2[0].replace(':','')
                        danci_3 = copy.deepcopy(danci)
                        danci_3[1][0] = fenjie + 1
                        danci_3[0] = 'u'
                        data_2.append(danci_2)
                        data_2.append(danci_3)


                    elif zifudingwei(tanngou,danci[0].replace(':',''),files_dir_1) == 'u':#把有冒号字母后面的那个字母单独拿出来

                        fenjie = (danci[1][0] + danci[1][1])//2
                        danci_2 = copy.deepcopy(danci)
                        danci_2[1][1] = fenjie
                        danci_2[0] = danci_2[0].replace(':','')
                        danci_3 = copy.deepcopy(danci)
                        danci_3[1][0] = fenjie + 1
                        danci_3[0] = 'u'
                        data_2.append(danci_2)
                        data_2.append(danci_3)

                    else:
                        data_2.append(danci)

                    break

        else:
            data_2.append(danci)#如果不是包函冒号的音素，就直接加入新的list

    # print(i)
    # print(data_danci)
    # print(data)
    # print(data_2)
    # os.system('pause')

    return data_2

#从chasen文件中把正解文的読み拿出来，准备给音素转化工具使用(C064L_chasen_1.txt)
import csv
import os
import jaconv#把片假名转化为平假名

def yomi(path_1):

    path = path_1
    for mulu in os.listdir(path):#每一个循环读到一个大文件C064L，C064R

        jushiqi = 0
        file_dir = os.path.join(path,mulu)
        #chasen的出力文件的地址以及整理之后的文件的地址

        file_dir_2 = os.path.join(file_dir,'keka')
        #原本的.out文件的路劲，仅仅是想要把文件名取出来

        feature = 'chasen.txt'
        feature_1 = 'chasen.ref'
        feature_2 = mulu +'_'+'chasen_1.txt'

        files_dir = os.path.join(file_dir,feature)

        save_dir = os.path.join(file_dir,feature_2)

        with open(files_dir,  'r',encoding='utf-8') as csvfile:

            reader = csv.reader(csvfile)

            column = [row for row in reader]

            column_2 = []

            for xiang in column:
                column_2.append(xiang[0].split())

            column_1 = []
            banyun = []

            for xiang in column_2:

                if len(xiang) == 1:

                    banyun.append(xiang[0])
                    column_1.append(banyun)
                    banyun = []

                else:
                    if xiang[0] != '、' and xiang[0] != '。':
                        if xiang[1] == '未知語':
                            banyun.append(xiang[0] + ' ' + jaconv.kata2hira(xiang[0]))
                        else:
                            banyun.append(xiang[0] + ' ' + jaconv.kata2hira(xiang[1]))
                        column_1.append(banyun)
                        banyun = []

            print(column_1)

            with open(save_dir, 'w', encoding='utf-8') as f:  # 把正解文一句一句地写入新的txt文件
                for xieru in column_1:
                    f.writelines(xieru[0] + '\n')

def zifudingwei(tanngou,danci,filelist):#把有冒号的字母后面的那个字母返回来

    print(filelist)
    print(tanngou)

    n = 0
    for y in tanngou:
        if y == danci:
            n = n+1
            return tanngou[n]
        n = n+1

yomi(path_1=r'C:\Users\tsukuba\Desktop\实验数据\symbol_2\train')
# qu(path_1=r'C:\Users\tsukuba\Desktop\实验数据\symbol_2\train')
logwen(path=r'C:\Users\tsukuba\Desktop\实验数据\symbol_2\train')
