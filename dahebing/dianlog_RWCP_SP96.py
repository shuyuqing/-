#根据原有的.out文件生成能被scoring所识别的标准日志文件
#把日志文件跟.ref文件一起输入scoring工具，就能获得带CCCCCSSSSS标志的文件了
#记住，必须要重新在linux中新建一个.ref文件，把在windows上生成的,ref文件的内容复制到这个新建的文件中去，才能被scoring识别
import csv
import os

def logwen(path):

    for mulu in os.listdir(path):

        basedir = os.path.join(path,mulu)

        file_dir = os.path.join(basedir,'keka')
        #原始的.out文件摆放的位置

        wenjianid = "Stat: adin_file: input speechfile: "
        #加入到out文件的第一句话

        file_dir_1 = basedir
        #生成新的log文件的存放地址

        banyun = []
        files_dir_1 = os.path.join(file_dir_1,"chasen.log")

        file_dir_list = os.listdir(file_dir)

        #注意，这部分是RWCP专用
        file_dir_list.sort(key=lambda ele: int(ele.split('_')[1]))  # 把每个元素都用split函数拆开，以第二个字符串的大小为基准，进行排序
        file_dir_list.sort(key=lambda ele: ele.split('_')[0])  # 然后再以拆开的第一个字符串为基准进行排序

        for i in file_dir_list:
        # for i in list:  # 循环读取同文件夹下的csv文件
            files_dir = os.path.join(file_dir,i)
            t = open(files_dir, 'r', encoding='utf-8')
            txtwenjian = csv.reader(t)  # encoding='utf-8'))#这一句代码看情况是否用
            data = [i for i in txtwenjian]
            # with open(files_dir,'r', encoding='utf-8') as f:#读取文本文件的时候一定要加上'r', encoding='utf-8'

            data.insert(0,wenjianid + i.replace(".out",".wav"))

            banyun.append(data[0])
            banyun.extend(data[1])

            # print(banyun)
            # os.system("pause")
            # files_dir_1 = os.path.join(file_dir_1,i.replace(".out",".log"))
        with open(files_dir_1, 'w',encoding='utf-8') as f:  # 把正解文一句一句地写入新的log文件
            for m in banyun:
                f.writelines(m+'\n')

            f.writelines(banyun[-2] + '\n')
            f.writelines(banyun[-1] + '\n')