#用于从chasen出力文件中取出已经分割好了的单词，然后把句子写入新的txt文件中
#首先我得通过认识结果把需要的正解文从.txt文件中取出来，写入到另外一个.txt文件中去
#之后就会得到.ref文件，然后去dianlog.py文本中操作
#记住，必须要重新在linux中新建一个.ref文件，把在windows上生成的,ref文件的内容复制到这个新建的文件中去，才能被scoring识别
import csv
import os
import jaconv#把片假名转化为平假名

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
        feature_2 = 'chasen_1.txt'

        files_dir = os.path.join(file_dir,feature)

        save_dir = os.path.join(file_dir,feature_2)

        with open(files_dir,  'r',encoding='utf-8') as csvfile:

            reader = csv.reader(csvfile)

            column = [row for row in reader]

            for reath in column:

                if 'reath' in reath:

                    print(files_dir)

qu(path_1=r'C:\Users\a7825\Desktop\新建文件夹\新建文件夹')