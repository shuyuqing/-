#ファイルはあるフォルダに存在しているかどうかを判断する
#想看看某个文件夹下面是否存在想要寻找的文件，把不存在的文件都输出来
import os,openpyxl

#检索的文件夹(检索范围)
path=r"C:\プロジェクト関係\最新ソース\20210201_全資産"

#想要找的文件名(一箇所にまとめました)
path_1=r"C:\プロジェクト関係\ファイル有無\合併_機能一覧×ソースの対応表.xlsx"

namelist=[]
filelist=[]
meiyou=[]

workbook = openpyxl.load_workbook(path_1)
sheet = workbook["ファイル一覧"]

for row_index_1 in range(1, 1251):
    name = sheet.cell(row=row_index_1, column=3).value
    namelist.append(name)

for root, dirs, files in os.walk(path):  # path 为根目录

    if len(files)!=0:
        for f in files:
            filelist.append(f)

    # print(files)
    # print(filelist)
    # os.system('pause')
flag=0

for n in namelist:

    for f in filelist:

        if n in f:

            flag=1

    if flag==0:

        meiyou.append(n)

    flag=0

#输出没有包含在文件夹里面的文件名
for m in meiyou:
    print(m)
