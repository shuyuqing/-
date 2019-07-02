import os,csv

path = r"C:\Users\a7825\Desktop\工作空间\跑代码\打标签\F1\C001\keka\L"
#包含语音文件的文件夹的路劲
newpath = r"C:\Users\a7825\Desktop\工作空间\语音数据\ogvc_16\F1\B"
#把制作好的正解文列表保存到这里

csv_path = r"C:\Users\a7825\Desktop\工作空间\跑代码\打标签\F1\C001\keka\LC001.txt"

str1 = r".wav"

# for name in os.listdir(path):
#
#     print(newname)
#     with open(newpath+'\A.csv', 'a') as f:  # 将结果保存为result.csv
#         f.write(newname + '\n')
newlist = []

txtwenjian = csv.reader(open(csv_path, 'r', encoding='utf-8'))
b = [i for i in txtwenjian]


for name in os.listdir(path):
    a = name[7:9]
    print(b[int(a)-1])
    newlist.append(b[int(a)-1])
# print(newlist)


