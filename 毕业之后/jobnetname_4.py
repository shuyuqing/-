import os,openpyxl

basedir_1=r"C:\bk\プロジェクト関係\シェル\PN"
basedir=r"C:\Users\1sn311\Desktop\ファイル名_シェル名(訂正版)_バージョン2.xlsx"
excel_path = r"C:\bk\プロジェクト関係\シェル\ファイル名_シェル名(訂正版)_新規作成.xlsx.xlsx"
path = r"C:\Users\1sn311\Desktop\ファイル名_シェル名(訂正版)_バージョン2.xlsx"
workbook = openpyxl.load_workbook(path)
sheet = workbook["PN"]
worksheet = workbook.create_sheet(title='新規作成')
biao1=[]
biao2=[]
biao3=[]
biao4=[]
dic={'':{}}


for dange in range(2,495):
    file_name = sheet.cell(row=dange, column=1).value
    sh_name = sheet.cell(row=dange, column=4).value
    xx = {file_name: {sh_name: 0}}
    dic.update(xx)

    if sh_name == "記述なし":

        biao1.append(" ")
        biao3.append(" ")
        biao4.append(" ")

    else:
        lujing = os.path.join(basedir_1, file_name)

        text_file = open(lujing, 'r')

        text = text_file.readlines()

        # print(text)
        for sh in text:

            # print(sh)
            ll = sh.split(",")

            # print(ll[0])
            # os.system('pause')

            if len(ll)>2:

                # print(sh_name)
                # print(ll[0])
                # print(ll[3])

                # os.system("pause")

                if len(ll)>6:

                    if sh_name in ll[0] or sh_name in ll[3] or sh_name in ll[2]  or sh_name in ll[6]:

                        if sh_name in ll[3] and sh_name !=  ll[0]:
                            # print(file_name)
                            # print(sh_name)
                            if dic[file_name][sh_name] == 0:
                                biao1.append(ll[2])
                                xx = {file_name: {sh_name: 1}}
                                dic.update(xx)
                                biao3.append(file_name)
                                biao4.append(sh_name)

                            # print(1)
                        elif sh_name in ll[0]:
                            # print(file_name)
                            # print(sh_name)
                            if dic[file_name][sh_name]==0:
                                biao1.append(ll[3])
                                xx = {file_name: {sh_name: 1}}
                                dic.update(xx)
                                biao3.append(file_name)
                                biao4.append(sh_name)

                        elif sh_name in ll[2]:
                            if dic[file_name][sh_name]==0:
                                biao1.append(ll[3])
                                xx = {file_name: {sh_name: 1}}
                                dic.update(xx)
                                biao3.append(file_name)
                                biao4.append(sh_name)

                        elif sh_name in ll[6]:
                            if dic[file_name][sh_name]==0:
                                biao1.append(ll[2])
                                xx = {file_name: {sh_name: 1}}
                                dic.update(xx)
                                biao3.append(file_name)
                                biao4.append(sh_name)
                else:
                    if sh_name in ll[3] and sh_name != ll[0]:
                        # print(file_name)
                        # print(sh_name)
                        if dic[file_name][sh_name] == 0:
                            biao1.append(ll[2])
                            xx = {file_name: {sh_name: 1}}
                            dic.update(xx)
                            biao3.append(file_name)
                            biao4.append(sh_name)

                        # print(1)
                    elif sh_name in ll[0]:
                        # print(file_name)
                        # print(sh_name)
                        if dic[file_name][sh_name] == 0:
                            biao1.append(ll[3])
                            xx = {file_name: {sh_name: 1}}
                            dic.update(xx)
                            biao3.append(file_name)
                            biao4.append(sh_name)

                    elif sh_name in ll[2]:
                        if dic[file_name][sh_name] == 0:
                            biao1.append(ll[3])
                            xx = {file_name: {sh_name: 1}}
                            dic.update(xx)
                            biao3.append(file_name)
                            biao4.append(sh_name)


# print(dic)
for ss in biao1:
    print(ss)
print(len(biao1))
                        
                
                        
                        # print(2)


                # else:
                #     biao1.append(ll[2])
            # print(file_name)
            # print(biao1)




