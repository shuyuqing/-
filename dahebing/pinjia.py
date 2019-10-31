#从chasen文件中把正解文的読み拿出来，准备给音素转化工具使用(C064L_chasen_1.txt)
import csv
import os
import jaconv#把片假名转化为平假名

def qu(path_1):

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

# qu(path_1=r'C:\Users\a7825\Desktop\新建文件夹\新建文件夹')