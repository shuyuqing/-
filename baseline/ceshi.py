import numpy as np
import os
#
# i = [[1,1],[1,0],[0,1]]
#
# i = np.array(i)
# print(i.shape)
#
# i = np.delete(i, [0,2], 0)
#
# print(i)


path = r'C:\Users\a7825\Desktop\工作空间\杂物\对比\symbol_40_16_16_biaoqian_pingheng\mizhichuli\all'

for i in os.listdir(path):

    path_1 = os.path.join(path,i)

    f = open(path_1, 'r')
    a = np.loadtxt(f, delimiter=',', skiprows=0).astype(np.float32)

    if len(a[0]) == 641:
        print(path_1)

        print(len(a[0]))
