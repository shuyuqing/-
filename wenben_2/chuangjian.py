import os
import muluzai as mu

path = r"C:\Users\a7825\Desktop\新建文件夹 (3)"#提供文件名列表
path_1 = r"C:\Users\a7825\Desktop\新建文件夹 (5)"#要把新建文件夹放在哪

mingdan = os.listdir(path)

for i in mingdan:

    path_2 = os.path.join(path_1,i.replace(os.path.splitext(i)[-1],''))#把文件的后缀名去掉
    mu.mkdir(path_2)

    path_wav = os.path.join(path_2,'wav')#想在生成的文件夹里创建什么文件夹都可以
    path_wav_all = os.path.join(path_2,'wav_all')
    path_keka = os.path.join(path_2,'keka')

    mu.mkdir(path_wav_all)
    mu.mkdir(path_wav)
    mu.mkdir(path_keka)
    file = open(os.path.join(path_2,i.replace(os.path.splitext(i)[-1],'')+'.txt'),'w')
    file_1 = open(os.path.join(path_2,'chasen.txt'),'w')