# 把cobolID_2.txt文件中的文件名取出来，然后把含有关键字的字符串拿出来(以円マーク为关键字对字符串进行拆分)
import os, openpyxl

# path = r"C:\Users\1sn311\Desktop\cobolID_2.txt"
path = r"C:\bk\プロジェクト関係\スクリプト\cobol\cobolID_2.txt"

text_file = open(path, 'r')
text = text_file.readlines()
liebiao1=[]
liebiao2=[]
# os.system('pause')

for w in text:

    # print(w)
    # os.system('pause')

    if 'PGMID=' in w or 'PRGID1=' in w or 'PRGID2=' in w or 'PRGID3=' in w or 'PRGID4=' in w or 'PRGID5=' in w or 'PRGID6='in w or 'PRGID7='in w or 'PRGID8='in w or 'PRGID9='in w or 'PRGID10='in w or 'PRGID11='in w or 'PRGID12='in w:
        # 以円マーク为关键字对字符串进行拆分
        ll = w.split('\\')

        al = ll[-1].split(' ')
        liebiao1.append(al[0])
        # print(al)

        for i in al:

            # print(i)

            if 'PGMID=' in i or 'PRGID1=' in i or 'PRGID2=' in i or 'PRGID3=' in i or 'PRGID4=' in i or 'PRGID5=' in i or 'PRGID6='in i or 'PRGID7='in i or 'PRGID8='in i or 'PRGID9='in i or 'PRGID10='in i or 'PRGID11='in i or 'PRGID12='in i:
                # print("sdhfk")
                # print(i)

                liebiao2.append(i)
        # os.system('pause')

for t in liebiao1:
    print(t)

# ll = text[11].split('\\')
#
# al=ll[-1].split(' ')
#
# liebiao1.append(al[0])
#
# for i in al:
#
#     if 'PRGID' in i:
#
#         liebiao2.append(i)


# workbook = openpyxl.load_workbook(path)
# sheet = workbook["PN"]
# worksheet = workbook.create_sheet(title='新規作成')
# biao1 = []
# biao2 = []
# biao3 = []
# biao4 = []
# dic = {'': {}}
#
# for dange in range(2, 495):
#     file_name = sheet.cell(row=dange, column=1).value
#     sh_name = sheet.cell(row=dange, column=4).value
#     xx = {file_name: {sh_name: 0}}
#     dic.update(xx)
#
#     if sh_name == "記述なし":
#
#         biao1.append(" ")
#         biao3.append(" ")
#         biao4.append(" ")
#
#     else:
#         lujing = os.path.join(basedir_1, file_name)
#
#         text_file = open(lujing, 'r')
#
#         text = text_file.readlines()
#
#         # print(text)
#         for sh in text:
#
#             # print(sh)
#             ll = sh.split(",")
#
#             # print(ll[0])
#             # os.system('pause')
#
#             if len(ll) > 2:
#
#                 # print(sh_name)
#                 # print(ll[0])
#                 # print(ll[3])
#
#                 # os.system("pause")
#
#                 if len(ll) > 6:
#
#                     if sh_name in ll[0] or sh_name in ll[3] or sh_name in ll[2] or sh_name in ll[6]:
#
#                         if sh_name in ll[3] and sh_name != ll[0]:
#                             # print(file_name)
#                             # print(sh_name)
#                             if dic[file_name][sh_name] == 0:
#                                 biao1.append(ll[2])
#                                 xx = {file_name: {sh_name: 1}}
#                                 dic.update(xx)
#                                 biao3.append(file_name)
#                                 biao4.append(sh_name)
#
#                             # print(1)
#                         elif sh_name in ll[0]:
#                             # print(file_name)
#                             # print(sh_name)
#                             if dic[file_name][sh_name] == 0:
#                                 biao1.append(ll[3])
#                                 xx = {file_name: {sh_name: 1}}
#                                 dic.update(xx)
#                                 biao3.append(file_name)
#                                 biao4.append(sh_name)
#
#                         elif sh_name in ll[2]:
#                             if dic[file_name][sh_name] == 0:
#                                 biao1.append(ll[3])
#                                 xx = {file_name: {sh_name: 1}}
#                                 dic.update(xx)
#                                 biao3.append(file_name)
#                                 biao4.append(sh_name)
#
#                         elif sh_name in ll[6]:
#                             if dic[file_name][sh_name] == 0:
#                                 biao1.append(ll[2])
#                                 xx = {file_name: {sh_name: 1}}
#                                 dic.update(xx)
#                                 biao3.append(file_name)
#                                 biao4.append(sh_name)
#                 else:
#                     if sh_name in ll[3] and sh_name != ll[0]:
#                         # print(file_name)
#                         # print(sh_name)
#                         if dic[file_name][sh_name] == 0:
#                             biao1.append(ll[2])
#                             xx = {file_name: {sh_name: 1}}
#                             dic.update(xx)
#                             biao3.append(file_name)
#                             biao4.append(sh_name)
#
#                         # print(1)
#                     elif sh_name in ll[0]:
#                         # print(file_name)
#                         # print(sh_name)
#                         if dic[file_name][sh_name] == 0:
#                             biao1.append(ll[3])
#                             xx = {file_name: {sh_name: 1}}
#                             dic.update(xx)
#                             biao3.append(file_name)
#                             biao4.append(sh_name)
#
#                     elif sh_name in ll[2]:
#                         if dic[file_name][sh_name] == 0:
#                             biao1.append(ll[3])
#                             xx = {file_name: {sh_name: 1}}
#                             dic.update(xx)
#                             biao3.append(file_name)
#                             biao4.append(sh_name)






