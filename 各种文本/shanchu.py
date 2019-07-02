#coding=utf-8
import os
import string

str1 ="vol1_dat_tsu1002_"

def re_name():


 for root, dirs, files in os.walk(os.getcwd()):
    for name in files:  # 遍历所有文件
        pos = name.find(str1)  # 把文件带有.out的字符删除
        if (pos == -1):
         continue
        newname = name[0:pos] + name[pos + len(str1):]
        os.rename(os.path.join(root, name), os.path.join(root, newname))

re_name()