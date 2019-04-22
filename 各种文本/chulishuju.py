import csv
import os

file_dir="C:/Users/a7825/Desktop/工作空间/语音数据/ASJ-JIPDEC/vol1/dat/can0001/i/shixulie/"
#原文件的路径
new_dir='C:/Users/a7825/Desktop/工作空间/语音数据/ASJ-JIPDEC/vol1/dat/can0001/i/新建文件夹/'
#处理过后的新文件的路径
#这两个路径最后的‘/’不能省略
for feature in os.listdir(file_dir):
    files_dir=file_dir+feature
    news_dir=new_dir+feature
    with open(files_dir) as f:

        reader=csv.reader(f)
        data=list(reader)
        #先把csv文件转化为list

        for i in range(len(data)):
            data[i].remove("'unknown'")
            #当需要删除的字符里面包含单引号时，外面要加一层双引号，如果需要删除的内容不是字符串而是
            #数字，那就用numpy解决吧
            data[i].remove('?')

        # with open('C:/Users/a7825/Desktop/工作空间/跑代码/lstm/zhu.csv', 'a+') as merge_file:
        with open(news_dir, 'wb') as f:
            for item in data:
                #从list中一个元素一个元素地写
                line = ','.join(item) + '\n'
                #把list写入csv文件中时，以逗号隔开每个元素，然后每个list写完之后回车（+ '/n'）
                f.write(line.encode('utf-8'))

