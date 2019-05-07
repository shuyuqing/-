import os

path = r'C:\Users\a7825\Desktop\工作空间\语音数据\RWCP-SP96-要切\新建文件夹\C1_M_10\wav'

dir_list = os.listdir(path)

# for i in dir_list:
#
#     print(i.split("_")[1])

dir_list.sort(key=lambda ele:  int(ele.split('_')[1]))#把每个元素都用split函数拆开，以第二个字符串的大小为基准，进行排序
dir_list.sort(key=lambda ele:  ele.split('_')[0])#然后再以拆开的第一个字符串为基准进行排序
print(dir_list)