#复制文件
import shutil,os

dir =r'C:\Users\a7825\Desktop\工作空间\语音数据\PASD_out\第一次实验\文件名'
#装有想要被复制的文件的文件夹的文件夹，最高级目录

desti =r'C:\Users\a7825\Desktop\工作空间\语音数据\UUDB\第一次实验\打标签\mizhichuli\all'
#目的地文件夹

wenjianjia = 'xinde_mizhichuli'
#装有特征值文件夹的文件名


for i in os.listdir(dir):

    dir_1 = os.path.join(dir,i)

    for e in os.listdir(dir_1):
        if e == wenjianjia:

            dir_2 = os.path.join(dir_1,wenjianjia)

            for u in os.listdir(dir_2):

                shutil.copy(os.path.join(dir_2,u), desti)