import os,csv

path = r"C:\Users\a7825\Desktop\工作空间\语音数据\CSJ\WAV\正解文\zhengjie_1"
#包含语音文件的文件夹的路劲

for name in os.listdir(path):
    path_1 = os.path.join(path,name)
    dakai = open(path_1, 'r', encoding='utf-8')
    txtwenjian = csv.reader(dakai)
    b = [i for i in txtwenjian]
    b_1 = []

    for y in b:
        u = y[0].split()
        u.pop(0) #把前两段都pop掉
        u.pop(0)
        b_1.append(''.join(u)) #把被分开的字符串再次合并起来，加入到新的列表里面


    dakai.close()

    with open(path_1, 'w',encoding='utf-8') as f:
        for u in b_1:
            f.writelines(u + '\n')  # 每写一句就空一行,把原来的文本都覆盖了
