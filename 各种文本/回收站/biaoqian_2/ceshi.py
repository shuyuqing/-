# coding=utf-8
#把文件夹里面的文件的名字都改了
import csv,os
import pipei as pi
path = r'C:\Users\a7825\Desktop\工作空间\语音数据\RWCP-SP96-要切\第一批 - 副本 (2)\C1_F_05\keka/l_1090_2300_C1_F_05.out'
#
# biaozhiwenjian = csv.reader(open(path, 'r', encoding='EUC-JP'))  # 把标志文件读进来
# b = [i for i in biaozhiwenjian]  # 转化为list
# # print(b)
# a=['72', 56, '76', 84, 80, 88]
# print(a.index('76'))
# for i in range(0,len(b),5):
#     print(b[i+4])

dianout = pi.read_out(path)#提取出来的帧号跟julius识别结果一样
print(dianout)
start = dianout.pop(0)[1][1]
print(start)
os.system('pause')
print(dianout)