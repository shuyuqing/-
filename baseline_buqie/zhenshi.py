import os
import re
import numpy as np
FRAMES_ADD = 1

def zhenshi(list):

    list_yuce = []
    list_yuce_1 = []

    for i in list:

        # print(i)
        # os.system('pause')

        if i[2] == 'C':

            # print(i[3],i[1][0],i[1][1])
            # os.system('pause')

            list_yuce_1 = [0 for i in range(int(i[1][0]),int(i[1][1])+1)]
            list_yuce.extend(list_yuce_1)

        else:

            # print(i[3], i[1][0], i[1][1])
            # os.system('pause')

            list_yuce_1 = [1 for i in range(int(i[1][0]),int(i[1][1])+1)]
            list_yuce.extend(list_yuce_1)

    # print(list_yuce)
    # print(len(list_yuce))

    # os.system('pause')
    list_yuce = np.array(list_yuce)

    return list_yuce




