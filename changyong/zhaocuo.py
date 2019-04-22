#作用于特征值文件，用于检查打标签的时候第一个空是不是全部被打上了1或者是0
import csv,os

dir = r'C:\Users\a7825\Desktop\工作空间\杂物\新建文件夹\RWCP\fbank\all'

for i in os.listdir(dir):

    a = csv.reader(open(os.path.join(dir,i), 'r'))

    for b in a:
        # print(b)
        # os.system("pause")
        if b[0]!='0' and b[0]!='1':
             print(i)

