import os, os.path, shutil

path = "C:/Users/a7825/Desktop/工作空间/杂物/写脚本/三个类的数据/识别结果 - 副本"

for x in os.listdir(path):
    fp = os.path.join(path, x)
    with open(fp, 'r', encoding='utf-8') as f:  # 打开文件
     lines = f.readlines(100)  # 读取所有行
     #first_line = lines[1]  # 取第一行
    print(lines)
