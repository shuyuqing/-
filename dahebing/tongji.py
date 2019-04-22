import os


def tongji(path):

    geshu = 0

    for path_1 in os.listdir(path):

        path_2 = os.path.join(path,path_1,'xinde_log')

        wenjian = os.listdir(path_2)

        size = len(wenjian)

        geshu = geshu + size

    print(geshu)

tongji(r'C:\Users\a7825\Desktop\工作空间\杂物\对比\ag1')
tongji(r'C:\Users\a7825\Desktop\工作空间\杂物\对比\symbol')

