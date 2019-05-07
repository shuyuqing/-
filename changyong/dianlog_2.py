#根据原有的.out文件生成能被scoring所识别的标准日志文件
#把日志文件跟.ref文件一起输入scoring工具，就能获得带CCCCCSSSSS标志的文件了
#记住，必须要重新在linux中新建一个.ref文件，把在windows上生成的,ref文件的内容复制到这个新建的文件中去，才能被scoring识别
import csv
import os

file_dir = r'C:\Users\a7825\Desktop\工作空间\语音数据\UUDB\第一次实验\打标签\第一批\C001L\keka'
#原始的.out文件摆放的位置

wenjianid = "Stat: adin_file: input speechfile: "
#加入到out文件的第一句话

file_dir_1 = r"C:\Users\a7825\Desktop\工作空间\语音数据\UUDB\第一次实验\打标签\第一批\C001L"
#生成新的log文件的存放地址


banyun = []
files_dir_1 = os.path.join(file_dir_1,"chasen.log")

for i in os.listdir(file_dir):
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
with open(files_dir_1, 'w',encoding='utf-8') as f:  # 把正解文一句一句地写入新的txt文件
    for m in banyun:
        f.writelines(m+'\n')
