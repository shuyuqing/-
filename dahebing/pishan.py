import os,shutil

def pishan(path,guanjianzi,guanjianzi_1):

    for wenjian in os.listdir(path):

        path_1 = os.path.join(path, wenjian, guanjianzi)

        if guanjianzi_1 == 'mulu':
            shutil.rmtree(path_1, True)#删除目录

        if guanjianzi_1 == 'wenjian':
            os.remove(path_1)#删除文件