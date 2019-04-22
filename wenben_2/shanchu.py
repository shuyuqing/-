import csv,os

path = r"C:\Users\a7825\Desktop\工作空间\语音数据\UUDB\var_out\C064\keka"

for name in os.listdir(path):

    csv_path = os.path.join(path,name)
    a = csv.reader(open(csv_path, 'r', encoding='utf-8'))

    b = [i for i in a]
    if len(b)==1:
        print(name)
