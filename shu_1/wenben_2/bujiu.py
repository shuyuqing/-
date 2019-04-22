import os
from shutil import copyfile

path_1 = r'C:\Users\a7825\Desktop\xuexi'
path_2 = r'C:\Users\a7825\Desktop\opentest'
path_new = r'C:\Users\a7825\Desktop\new'
#
mingdan_1 = os.listdir(path_1)
mingdan_2 = os.listdir(path_2)

# for i in mingdan_1:
#
#     if 'csv_1.csv' in i:
#
#         os.remove(os.path.join(path_1,i))

jishuqi = 0

mingdan_1_1 = os.listdir(path_1)

for i in mingdan_1_1:

    if jishuqi<1107:

        if i not in mingdan_2:

            copyfile(os.path.join(path_1, i),os.path.join(path_new,i))  # 自动复制

            jishuqi+=1






