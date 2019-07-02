#注意，顺序一定要先给正解文加句号，然后再分别提取对应的正解文
#注意，生成正解文是在把空的.out文件都删干净之后，再把多余的.wav文件删掉，最后才来做的一个步骤
#正解文是从跟文件夹同名的txt文本中提取的
import os,csv
import jiajuhao as jj

path = r"C:\Users\a7825\Desktop\工作空间\语音数据\RWCP-SP96-要切\第三批"#批次

jj.juhao(path)

for filename in os.listdir(path):

    path_zhengjie = os.path.join(path,filename,filename+'.txt')
    dakai = open(path_zhengjie, 'r', encoding='utf-8')
    path_keka = os.path.join(path,filename,'keka')

    mingdan = os.listdir(path_keka)

    zhengjie_xuhao_b = []
    zhengjie_xuhao_a = []

    for y in mingdan:
        fenkai = y.split('_', 2)

        if fenkai[0] == 'l':
            zhengjie_xuhao_b.append(int(fenkai[1]))

        elif fenkai[0] == 'r':
            zhengjie_xuhao_a.append(int(fenkai[1]))

    # print("输出文件名")
    # print(filename)
    # zhengjie_xuhao_b.sort()
    # zhengjie_xuhao_a.sort()
    # print("输出zhengjie_b")
    # print(zhengjie_xuhao_b)
    # print("输出zhengjie_a")
    # print(zhengjie_xuhao_a)
    # os.system('pause')

    txtwenjian = csv.reader(dakai)
    b = [i for i in txtwenjian]

    zhengjiewen_b = []
    zhengjiewen_a = []

    for n in range(len(b)):

        print(filename)
        print(n)
        if b[n] != '':
            b[n][0] = b[n][0].replace('。','')
            # print(b[n][0])
            # os.system("pause")

            if b[n][0] == 'B':#记住B是left

                zhengjie_b = b[n+3][0]
                # print(zhengjie_b)
                # os.system('pause')
                b[n+1][0] = b[n+1][0].replace('。','')
                if int(b[n+1][0]) in zhengjie_xuhao_b:

                    zhengjiewen_b.append(zhengjie_b)

            elif b[n][0] == 'A':#A是right

                zhengjie_a = b[n+3][0]

                b[n+1][0] = b[n+1][0].replace('。', '')

                if int(b[n+1][0]) in zhengjie_xuhao_a:

                    zhengjiewen_a.append(zhengjie_a)

    path_zhengjie_b = os.path.join(path,filename,'l_' + filename + '.txt')
    path_zhengjie_a = os.path.join(path, filename, 'r_' + filename + '.txt')

    with open(path_zhengjie_b, 'w',encoding='utf-8') as f:# 把正解文一句一句地写入新的txt文件

        for u in zhengjiewen_b:
            f.writelines(u + '\n')  # 每写一句就空一行

    with open(path_zhengjie_a, 'w',encoding='utf-8') as f:

        for u in zhengjiewen_a:
            f.writelines(u + '\n')  # 每写一句就空一行

    dakai.close()