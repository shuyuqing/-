import numpy as np
import os


# path_baocun = r'C:\Users\a7825\Desktop\工作空间\语音数据\新建文件夹'
# path_name = 'wenjian.npz'
#
#
# shuzu_1 = np.array([[1,2,3],[1,2,4]])
# shuzu_2 = np.array([[1,3,2],[2,3,1]])
# shuzu_3 = np.array([[2,1,3],[2,4,5]])
# shuzu_4 = np.array([[3,4,5],[2,7,8]])
#
#
#
# path_baocun = os.path.join(path_baocun,path_name)
#
# np.savez(path_baocun, shuzu_2, shuzu_1, shuzu_3, shuzu_4)  # 把矩阵保存成npz文件
#
# wenjian = np.load(path_baocun)
#
# print(wenjian['arr_0'])
path_baocun = r'C:\Users\a7825\Desktop\40_8_8/train.npz'

wenjian = np.load(path_baocun)

print(wenjian['arr_1'].shape)
print(wenjian['arr_0'].shape)
# print(wenjian['arr_0'][0])
# print(wenjian['arr_1'][0])
# start = 0
# end = start+40

# print(wenjian['arr_0'][41:81])
# print(wenjian['arr_0'][41])
# print(wenjian['arr_0'][82])
# print(wenjian['arr_0'][123])
# print(wenjian['arr_0'][164])


# for i in range(508640):
#
#     print(wenjian['arr_1'][start:end])

# print(wenjian['arr_1'][0:44])


