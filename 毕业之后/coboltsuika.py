#当需要处理一个key对应一串值的时候就用dic={'':[]}
import os, openpyxl

path = r"C:\プロジェクト関係\other\cobol名2.xlsx"
path1= r"C:\プロジェクト関係\other\プロセス名、プロセスId、シェル名の関係を洗い出し.xlsx"
excel_path = r"C:\プロジェクト関係\other\新規作成.xlsx"

#键值对的格式为string:list
dic={'':[]}
sheru_2=""
a=[]
workbook=openpyxl.load_workbook(path)
sheet = workbook["Sheet1"]


for i in range(1,687):

    sheru=sheet.cell(row=i, column=1).value
    cobol=sheet.cell(row=i, column=2).value

    if sheru==sheru_2:

        #更新dictionary
        a.append(cobol)
        xx = {sheru: a}
        dic.update(xx)

    else:
        a=[]
        a.append(cobol)
        xx = {sheru: a}
        dic.update(xx)

    sheru_2=sheru

workbook1 = openpyxl.load_workbook(path1)
sheet1 = workbook1["4.5.2.4.キャンペーン"]

worksheet = workbook1.create_sheet(title='新規作成')

liebiao=[]
index=2

worksheet.cell(row=1, column=1).value = 'プロセス名'
worksheet.cell(row=1, column=2).value = 'プロセスID'
worksheet.cell(row=1, column=3).value = 'シェルID'
worksheet.cell(row=1, column=4).value = 'プログラムID'

for i in range(2,24):
    promei=sheet1.cell(row=i, column=1).value
    proid=sheet1.cell(row=i, column=2).value
    syeruid=sheet1.cell(row=i, column=3).value

    #如果字典里面有这个key
    if syeruid in dic.keys():

        for j in dic[syeruid]:

            worksheet.cell(row=index, column=1).value = promei
            worksheet.cell(row=index, column=2).value = proid
            worksheet.cell(row=index, column=3).value = syeruid
            worksheet.cell(row=index, column=4).value = j
            index+=1
    else:

        worksheet.cell(row=index, column=1).value = promei
        worksheet.cell(row=index, column=2).value = proid
        worksheet.cell(row=index, column=3).value = syeruid
        worksheet.cell(row=index, column=4).value = "記述なし"
        index += 1

workbook1.save(excel_path)
workbook.close()

