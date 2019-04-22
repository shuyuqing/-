import csv
#原来csv这个包是可以处理txt文件的
import os

file_dir=r"C:\Users\a7825\Desktop\正解文/"
#原文件的路径
new_dir1=r"C:\Users\a7825\Desktop\分类L/"
new_dir2=r"C:\Users\a7825\Desktop\分类R/"
#处理过后的新文件的路径
#这两个路径最后的‘/’不能省略
for feature in os.listdir(file_dir):
    files_dir=file_dir+feature
    news_dir1=new_dir1+feature
    news_dir2=new_dir2+feature
    with open(files_dir) as f:

        reader = csv.reader(f)
        data = list(reader)
        print(len(data))
        with open(news_dir1, 'wb') as f:
            for i in data:
                print(i)
                if i[0].split(":",2)[0]=='L':
                    # print(i[0].split(":",2)[0])
                    #每一行的内容被写入了listi,然后以冒号为分隔符，分成两段，选取第一段
                    #从list中一个元素一个元素地写
                    line = i[0]
                    #把list写入csv文件中时，以逗号隔开每个元素，然后每个list写完之后回车（+ '/n'）
                    #要想要回车符号+/n起作用，就不能重复打开文件，打开一次就要把所有句子写进去
                    f.write(line.encode('utf-8')+'\n'.encode('utf-8'))

        with open(news_dir2, 'wb') as g:
            for i in data:
                print(i)
                if i[0].split(":",2)[0]=='R':
                    # print(i[0].split(":",2)[0])
                    #每一行的内容被写入了listi,然后以冒号为分隔符，分成两段，选取第一段
                    #从list中一个元素一个元素地写
                    line = i[0]
                    #把list写入csv文件中时，以逗号隔开每个元素，然后每个list写完之后回车（+ '/n'）
                    g.write(line.encode('utf-8')+'\n'.encode('utf-8'))





