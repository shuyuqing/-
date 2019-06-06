import os
import numpy as np
import muluzai as mu
import shutil


def qiexiao(path,wenjian_1,path_new):

            path_2 = path
            f = open(path_2, 'r')
            a = np.loadtxt(f, delimiter=',', skiprows=0).astype(np.float32)
            Labeltrain = a[:, 0:1]
            f.close()
            # os.remove(path_2)

            jishuqi_0 = 0
            jishuqi_1 = 0
            zhizhen_tou = 0
            zhizhen_wei = 0
            beiqie = 1

            while True:

                    print(path_2)
                    while Labeltrain[zhizhen_wei] == Labeltrain[zhizhen_tou]:

                        jishuqi_0 += 1

                        zhizhen_wei += 1

                    zhizhen_yanshen = zhizhen_wei

                    while Labeltrain[zhizhen_yanshen] == Labeltrain[zhizhen_wei]:

                        jishuqi_1 += 1

                        if zhizhen_wei == len(Labeltrain) - 1:#如果指针已经到了尾部

                            zhizhen_wei += 1

                            if jishuqi_0 < jishuqi_1:  # 上短下长

                                zhizhen_qie = zhizhen_tou + (jishuqi_0 * 2)
                                qiele = a[zhizhen_tou:zhizhen_qie]
                                np.savetxt(path_new + "/" + wenjian_1 + '_' + str(beiqie) + ".csv", qiele,
                                           delimiter=',')

                            elif jishuqi_0 == jishuqi_1:
                                qiele = a[zhizhen_tou:zhizhen_wei]
                                np.savetxt(path_new + "/" + wenjian_1 + '_' + str(beiqie) + ".csv", qiele,
                                           delimiter=',')

                            else:

                                zhizhen_qie = zhizhen_wei - (jishuqi_1 * 2)
                                qiele = a[zhizhen_qie:zhizhen_wei]
                                np.savetxt(path_new + "/" + wenjian_1 + '_' + str(beiqie) + ".csv", qiele,
                                           delimiter=',')
                            return

                        zhizhen_wei += 1

                    if jishuqi_0 < jishuqi_1:#上短下长

                        zhizhen_qie = zhizhen_tou + (jishuqi_0 * 2)
                        qiele = a[zhizhen_tou:zhizhen_qie]
                        np.savetxt(path_new + "/" + wenjian_1 + '_' + str(beiqie) + ".csv", qiele, delimiter=',')

                    elif jishuqi_0 == jishuqi_1:
                        qiele = a[zhizhen_tou:zhizhen_wei]
                        np.savetxt(path_new + "/" + wenjian_1 + '_' + str(beiqie) + ".csv", qiele, delimiter=',')


                    else:

                        zhizhen_qie = zhizhen_wei - (jishuqi_1 * 2)
                        qiele = a[zhizhen_qie:zhizhen_wei]
                        np.savetxt(path_new + "/" + wenjian_1 + '_' + str(beiqie) + ".csv", qiele, delimiter=',')

                    jishuqi_1 = 0
                    jishuqi_0 = 0
                    beiqie += 1
                    zhizhen_tou = zhizhen_yanshen
                    zhizhen_wei = zhizhen_yanshen

