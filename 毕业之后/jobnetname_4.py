#シェル名を作成
import os,openpyxl

basedir_1=r'C:\プロジェクト関係\シェル(個別層)\OT'
path = r"C:\プロジェクト関係\ドキュメント\二回目\ファイル名_cobol名.xlsx"
workbook = openpyxl.load_workbook(path)
sheet = workbook['OT']
worksheet = workbook.create_sheet(title='新規作成')
biao1=[]
biao2=[]
biao3=[]
biao4=[]
dic={'':{}}


for dange in range(1,86):
    file_name = sheet.cell(row=dange, column=1).value
    sh_name = sheet.cell(row=dange, column=2).value
    xx = {file_name: {sh_name: 0}}
    dic.update(xx)

    if sh_name == "記述なし":

        biao1.append("記述なし")
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
# print(len(biao1))
                        





