# coding=utf-8
import os
import string

str1 = ".log"

dir = r'C:\Users\a7825\Desktop\工作空间\语音数据\UUDB\第一次实验\all_log'

    # 拼接字符串，把单引号改成双引号居然好使
def re_name():
    for root, dirs, files in os.walk(dir):#获取当前目录下的文件名
        for name in files:  # 遍历所有文件
            pos = name.find(str1)  # 把文件名中的str1的字符删除
            if (pos == -1):
                continue
            newname = name.replace(str1,'')
            os.rename(os.path.join(root, name), os.path.join(root, newname))


re_name()