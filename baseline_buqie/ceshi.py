import os
import numpy as np
path = r'C:\Users\a7825\Desktop\新しいフォルダー\ag1_40_16_biaoqian_pingheng\mizhichuli\all'

for i in os.listdir(path):

    path_1 = os.path.join(path,i)

    f = open(path_1, 'r')
    a = np.loadtxt(f, delimiter=',', skiprows=0).astype(np.float32)

    if len(a[0]) != 321:
        print(path_1)

        print(len(a[0]))
