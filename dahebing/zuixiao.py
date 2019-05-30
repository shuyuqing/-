import os,shutil,csv
import numpy as np

def zuixiao(path,guanjianzi):  # 把标签都是1的文件找出来

    liebiao = os.listdir(path)

    for name in liebiao:

        path_mizhichuli = os.path.join(path, name, guanjianzi)

        for name_1 in os.listdir(path_mizhichuli):

            path_2 = os.path.join(path_mizhichuli, name_1)

            f = open(path_2, 'r', encoding='utf-8')
            tezhengzhi = csv.reader(f)
            t_file_list = [i for i in tezhengzhi]
            f.close()

            if len(t_file_list) <= 10:
                print('移除文件')
                print(path_2)

                os.remove(path_2)