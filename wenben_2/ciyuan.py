import os
import numpy as np

path = r'C:\Users\a7825\Desktop\工作空间\杂物\对比\symbol_1\symbol_40_8_16_biaoqian_pingheng_train\mizhichuli\all'
ciyuan = 321

for name in os.listdir(path):

    path_1 = os.path.join(path,name)
    tezheng = np.loadtxt(path_1, delimiter=',')

    if int(tezheng.shape[1]) != ciyuan:

        print(path)
