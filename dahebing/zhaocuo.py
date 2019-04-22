#作用于特征值文件，用于检查打标签的时候第一个空是不是全部被打上了1或者是0
import csv,os

def zhaocuo(path):

    dir = os.path.join(path,'data')

    label_all = 0
    label_1 = 0

    path_1 = os.path.join(dir,'fbank','all')

    for i in os.listdir(path_1):

        a = csv.reader(open(os.path.join(path_1,i), 'r'))

        for b in a:

            label_all = label_all + 1
            # print(b)
            # os.system("pause")
            # print(float(b[0]))
            if str(int(float(b[0])))!='0' and str(int(float(b[0])))!='1':
                 print('%s这个文件的标签有问题'%i)
                 os.system("pause")

            if str(int(float(b[0]))) == '1':
                label_1 = label_1 + 1

    print("这批数据中标签是1的数据占了百分之%f"%((label_1/label_all)*100))

