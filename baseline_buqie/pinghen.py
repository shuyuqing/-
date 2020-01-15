import os
import numpy as np
import dahebing.muluzai as mu
import shutil

def ping(list):

    jishuqi_0 = 0
    jishuqi_1 = 0
    zhizhen_tou = 0
    zhizhen_wei = 0
    beiqie = 1
    list_chongzao = []
    list_chongzao_1 = []
    list_zong = []

    while True:

            while list[1][zhizhen_wei] == list[1][zhizhen_tou]:

                jishuqi_0 += 1

                zhizhen_wei += 1

            zhizhen_yanshen = zhizhen_wei

            while list[1][zhizhen_yanshen] == list[1][zhizhen_wei]:

                jishuqi_1 += 1

                if zhizhen_wei == len(list[1]) - 1:#如果指针已经到了尾部

                    zhizhen_wei += 1

                    if jishuqi_0 < jishuqi_1:  # 上短下长

                        # print('经过1')

                        zhizhen_qie = zhizhen_tou + (jishuqi_0 * 2)

                        list_chongzao = []

                        list_chongzao.append(np.array(list[1][zhizhen_tou:zhizhen_qie]))

                        list_chongzao.append(np.array(list[0][zhizhen_tou:zhizhen_qie]))

                        list_chongzao_1.append(list_chongzao)

                    elif jishuqi_0 == jishuqi_1:

                        # print('经过2')

                        list_chongzao = []

                        qiele = list[1][zhizhen_tou:zhizhen_wei]
                        list_chongzao.append(np.array(qiele))
                        list_chongzao.append(np.array(list[0][zhizhen_tou:zhizhen_wei]))
                        list_chongzao_1.append(list_chongzao)

                    else:

                        list_chongzao = []
                        # print("经过3")

                        zhizhen_qie = zhizhen_wei - (jishuqi_1 * 2)
                        qiele = list[1][zhizhen_qie:zhizhen_wei]
                        list_chongzao.append(np.array(qiele))
                        list_chongzao.append(np.array(list[0][zhizhen_qie:zhizhen_wei]))

                        list_chongzao_1.append(list_chongzao)

                    # list_chongzao_1 = np.array(list_chongzao_1)

                    # print('有了')

                    return list_chongzao_1

                zhizhen_wei += 1

            if jishuqi_0 < jishuqi_1:#上短下长

                zhizhen_qie = zhizhen_tou + (jishuqi_0 * 2)

                list_chongzao = []

                qiele = list[1][zhizhen_tou:zhizhen_qie]
                list_chongzao.append(np.array(qiele))
                list_chongzao.append(np.array(list[0][zhizhen_tou:zhizhen_qie]))

                list_chongzao_1.append(list_chongzao)
                # print("经过4")

            elif jishuqi_0 == jishuqi_1:

                qiele = list[1][zhizhen_tou:zhizhen_wei]

                list_chongzao = []

                list_chongzao.append(np.array(qiele))
                list_chongzao.append(np.array(list[0][zhizhen_tou:zhizhen_wei]))

                list_chongzao_1.append(list_chongzao)
                # print("经过5")

            else:

                list_chongzao = []
                zhizhen_qie = zhizhen_wei - (jishuqi_1 * 2)
                qiele = list[1][zhizhen_qie:zhizhen_wei]
                list_chongzao.append(np.array(qiele))
                list_chongzao.append(np.array(list[0][zhizhen_qie:zhizhen_wei]))

                list_chongzao_1.append(list_chongzao)
                # print("经过6")

            jishuqi_1 = 0
            jishuqi_0 = 0
            beiqie += 1
            zhizhen_tou = zhizhen_yanshen
            zhizhen_wei = zhizhen_yanshen