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

            label_1 = 0
            label_all = 0

            for b in Labeltrain:

                label_all = label_all + 1

                if b == 1:
                    label_1 = label_1 + 1

            baifenbi = (label_1 / label_all) * 100

            print(wenjian_1)
            print(baifenbi)

            if baifenbi <= 38:#标签1的比例低于40%就切

                jishuqi_1 = 0
                jishuqi_0 = 0
                zhizhen_tou = 0
                zhizhen_wei = 0
                beiqie = 1

                while True:

                    if Labeltrain[zhizhen_wei] == 1:

                        while Labeltrain[zhizhen_wei] == 1:

                            if zhizhen_wei == len(Labeltrain) - 1:

                                print("看1")
                                qiele = a[zhizhen_tou:]
                                np.savetxt(path_new + "/" + wenjian_1 + '_' + str(beiqie) + ".csv", qiele, delimiter=',')
                                return

                            jishuqi_1 += 1
                            zhizhen_wei += 1

                        while Labeltrain[zhizhen_wei] == 0:

                            if zhizhen_wei == len(Labeltrain) - 1:

                                print("看2")
                                qiele = a[zhizhen_tou:]
                                np.savetxt(path_new + "/" + wenjian_1 + '_' + str(beiqie) + ".csv", qiele, delimiter=',')
                                return

                            jishuqi_0 += 1
                            zhizhen_wei += 1

                            if zhizhen_wei < len(Labeltrain) - 1:

                                if jishuqi_0 == jishuqi_1:
                                    print('看3')
                                    qiele = a[zhizhen_tou:zhizhen_wei]

                                    np.savetxt(path_new + "/" + wenjian_1 + '_' + str(beiqie) + ".csv", qiele, delimiter=',')

                                    jishuqi_1 = 0
                                    jishuqi_0 = 0
                                    beiqie += 1
                                    zhizhen_tou = zhizhen_wei
                                    break

                    elif Labeltrain[zhizhen_wei] == 0:

                        while Labeltrain[zhizhen_wei] == 0:

                            if zhizhen_wei == len(Labeltrain) - 1:

                                print("看4")
                                qiele = a[zhizhen_tou:]
                                np.savetxt(path_new + "/" + wenjian_1 + '_' + str(beiqie) + ".csv", qiele, delimiter=',')
                                return

                            jishuqi_0 += 1
                            zhizhen_wei += 1

                            if zhizhen_wei < len(Labeltrain) - 1:

                                if jishuqi_0 == jishuqi_1:

                                    qiele = a[zhizhen_tou:zhizhen_wei]
                                    print("看5")
                                    np.savetxt(path_new + "/" + wenjian_1 + '_' + str(beiqie) + ".csv", qiele,
                                               delimiter=',')

                                    jishuqi_1 = 0
                                    jishuqi_0 = 0
                                    beiqie += 1
                                    zhizhen_tou = zhizhen_wei
                                    break

                        while Labeltrain[zhizhen_wei] == 1:

                            if zhizhen_wei < len(Labeltrain) - 1:

                                jishuqi_1 += 1
                                zhizhen_wei += 1

                            else:

                                qiele = a[zhizhen_tou:]

                                print("看6")
                                np.savetxt(path_new + "/" + wenjian_1 + '_' + str(beiqie) + ".csv", qiele,
                                           delimiter=',')

                                return

                        if jishuqi_1 < jishuqi_0:

                            if zhizhen_wei == len(Labeltrain) - 1:

                                print("看7")
                                zhizhen_tou = zhizhen_wei - (2*jishuqi_1)

                                qiele = a[zhizhen_tou:]

                                np.savetxt(path_new + "/" + wenjian_1 + '_' + str(beiqie) + ".csv", qiele, delimiter=',')

                                return

                            else:
                                print("看8")
                                zhizhen_tou = zhizhen_wei - (2*jishuqi_1)

                                qiele = a[zhizhen_tou:zhizhen_wei]

                                np.savetxt(path_new + "/" + wenjian_1 + '_' + str(beiqie) + ".csv", qiele,
                                           delimiter=',')
                                jishuqi_1 = 0
                                jishuqi_0 = 0
                                beiqie += 1
                                zhizhen_tou = zhizhen_wei

            else:#如果没有被切，就直接把文件复制到closetest_1的文件夹里面去。

                print("开始复制文件")
                print(path_2)
                print(os.path.join(path_new,os.path.split(path_2)[1]))
                print("复制文件结束")
                shutil.copy(path_2,os.path.join(path_new,os.path.split(path_2)[1]))