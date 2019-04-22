import os,shutil

def zhuanyi(path,dizhi_1,dizhi_2):

    for wenjian in os.listdir(path):

        path_1 = os.path.join(path, wenjian, dizhi_1)
        path_2 = os.path.join(path, wenjian, dizhi_2)

        for wenjian_1 in os.listdir(path_1):

            path_1_1 = os.path.join(path_1, wenjian_1)

            shutil.move(path_1_1,path_2)