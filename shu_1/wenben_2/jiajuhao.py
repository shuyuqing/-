#操作顺序是先在每句正解文的最后加上一个句号，然后再从中按序号提取需要的正解文
import csv
import os


def juhao(path_1):

    path = path_1
    for feature in os.listdir(path):

        path_2 = os.path.join(path, feature, feature+'.txt')
        t = open(path_2, 'r',encoding='utf-8')

        txtwenjian = csv.reader(t)# encoding='utf-8'这一句代码看情况是否用
        data = [i for i in txtwenjian]
        # with open(files_dir,'r', encoding='utf-8') as f:#读取文本文件的时候一定要加上'r', encoding='utf-8'
        # print(data)

        for b in data:

            b[0] = b[0].replace('，', '、')#把句子里面的逗号换成、
            b[0] = b[0].replace('.','')#把句子里面的.删掉

            if not b[0].endswith('。'):#如果句子不是以。结尾就加上。
                b[0] = b[0] + '。'#这样的迭代就可以把list里面的值全部都修改了

            if b[0].endswith('、。'):
                b[0] = b[0].replace('、。','。')

        # print(data)
        # os.system('pause')
        # with open('C:/Users/a7825/Desktop/工作空间/跑代码/lstm/zhu.csv', 'a+') as merge_file:
        t.close()
        with open(path_2, 'w', encoding='utf-8') as m:
            for item in data:
                item[0] = item[0] + '\n'
                # #从list中一个元素一个元素地写
                # line = ','.join(item) + '\n'
                m.write(str(item[0]))