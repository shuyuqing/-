import os
import numpy as np
import muluzai as mu

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

            if baifenbi <= 45:

                jishuqi_1 = 0
                jishuqi_0 = 0
                zhizhen_tou = 0
                zhizhen_wei = 0
                beiqie = 1

                while True:

                    if Labeltrain[zhizhen_wei] == 1:

                        while Labeltrain[zhizhen_wei] == 1:

                            jishuqi_1 += 1
                            zhizhen_wei += 1

                        while Labeltrain[zhizhen_wei] == 0:

                            jishuqi_0 += 1
                            zhizhen_wei += 1

                            if zhizhen_wei < len(Labeltrain) - 1:

                                if jishuqi_0 == jishuqi_1:
                                    print('看1')
                                    qiele = a[zhizhen_tou:zhizhen_wei]

                                    np.savetxt(path_new + "/" + wenjian_1 + '_' + str(beiqie) + ".csv", qiele, delimiter=',')

                                    jishuqi_1 = 0
                                    jishuqi_0 = 0
                                    beiqie += 1
                                    zhizhen_tou = zhizhen_wei
                                    break

                            else:
                                print("看2")
                                qiele = a[zhizhen_tou:]
                                np.savetxt(path_new + "/" + wenjian_1 + '_' + str(beiqie) + ".csv", qiele,delimiter=',')

                                return

                    elif Labeltrain[zhizhen_wei] == 0:

                        while Labeltrain[zhizhen_wei] == 0:

                            jishuqi_0 += 1
                            zhizhen_wei += 1

                            if zhizhen_wei < len(Labeltrain) - 1:

                                if jishuqi_0 == jishuqi_1:

                                    qiele = a[zhizhen_tou:zhizhen_wei+1]
                                    print("看3")
                                    np.savetxt(path_new + "/" + wenjian_1 + '_' + str(beiqie) + ".csv", qiele,
                                               delimiter=',')

                                    jishuqi_1 = 0
                                    jishuqi_0 = 0
                                    beiqie += 1
                                    zhizhen_tou = zhizhen_wei
                                    break

                            else:

                                qiele = a[zhizhen_tou:]
                                print("看4")

                                np.savetxt(path_new + "/" + wenjian_1 + '_' + str(beiqie) + ".csv", qiele,
                                           delimiter=',')

                                return

                        while Labeltrain[zhizhen_wei] == 1:

                            if zhizhen_wei < len(Labeltrain) - 1:

                                jishuqi_1 += 1
                                zhizhen_wei += 1

                            else:

                                qiele = a[zhizhen_tou:]

                                print("看5")
                                np.savetxt(path_new + "/" + wenjian_1 + '_' + str(beiqie) + ".csv", qiele,
                                           delimiter=',')

                                return

                        if jishuqi_1 <= jishuqi_0:

                            if zhizhen_wei == len(Labeltrain) - 1:

                                print("看6")
                                zhizhen_tou = zhizhen_wei - (2*jishuqi_1)

                                qiele = a[zhizhen_tou:]

                                np.savetxt(path_new + "/" + wenjian_1 + '_' + str(beiqie) + ".csv", qiele, delimiter=',')

                                return

                            else:
                                print("看7")
                                zhizhen_tou = zhizhen_wei - (2*jishuqi_1)

                                qiele = a[zhizhen_tou:zhizhen_wei]

                                np.savetxt(path_new + "/" + wenjian_1 + '_' + str(beiqie) + ".csv", qiele,
                                           delimiter=',')
                                jishuqi_1 = 0
                                jishuqi_0 = 0
                                beiqie += 1
                                zhizhen_tou = zhizhen_wei

                        else:

                            while Labeltrain[zhizhen_wei] == 0:
                                jishuqi_0 += 1
                                zhizhen_wei += 1

                                if zhizhen_wei < len(Labeltrain) - 1:

                                    if jishuqi_0 == jishuqi_1:
                                        qiele = a[zhizhen_tou:zhizhen_wei]

                                        print("看8")

                                        np.savetxt(path_new + "/" + wenjian_1 + '_' + str(beiqie) + ".csv", qiele,
                                                   delimiter=',')

                                        jishuqi_1 = 0
                                        jishuqi_0 = 0
                                        beiqie += 1
                                        zhizhen_tou = zhizhen_wei
                                        break

                                else:
                                    print("看9")
                                    qiele = a[zhizhen_tou:]
                                    np.savetxt(path_new + "/" + wenjian_1 + '_' + str(beiqie) + ".csv", qiele,
                                               delimiter=',')
                                    return