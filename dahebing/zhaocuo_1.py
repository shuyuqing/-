#作用于特征值文件，用于检查打标签的时候第一个空是不是全部被打上了1或者是0
import csv,os
import numpy as np

def zhaocuo(path,guanjianzi):

    for name in os.listdir(path):

        path_xinde_log = os.path.join(path,name,guanjianzi)

        for name_1 in os.listdir(path_xinde_log):

            path_xinde_log_1 = os.path.join(path_xinde_log,name_1)

            # print(path_xinde_log_1)

            # a = np.loadtxt(path_xinde_log_1, delimiter=',', skiprows=0).astype(np.float32)
            #
            # Labeltrain = a[:, 0:1]

            f = open(path_xinde_log_1, 'r', encoding='utf-8')
            tezhengzhi = csv.reader(f)
            t_file_list = [i for i in tezhengzhi]
            f.close()

            for i in t_file_list:

                if i[0]!='1' and i[0]!='0':

                    print("这个文件的标签不是0或1")
                    print(path_xinde_log_1)
                    # os.remove(path_xinde_log_1)

                    break


# zhaocuo(path=r'C:\Users\a7825\Desktop\新建文件夹 (6)',guanjianzi=r'log_biaoqian')
