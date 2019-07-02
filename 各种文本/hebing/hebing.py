import os
import pandas as pd
import glob


# 定义函数hebing

def hebing():
    list = glob.glob('*.csv')  # 查看同文件夹下的csv文件数

    print(u'共发现%s个CSV文件' % len(list))
    print(u'正在处理............')
    for i in list:  # 循环读取同文件夹下的csv文件
        fr = open(i, 'r').read()
        with open('result.csv', 'a') as f:  # 将结果保存为result.csv
            f.write(fr)
    print(u'合并完毕！')


if __name__ == '__main__':
 hebing()



