import os,openpyxl

basedir=r'C:\Users\1sn311\Desktop\新しいフォルダー (3)\10_ジョブネット定義\0'
# excel_path = r"C:\プロジェクト関係\ドキュメント\二回目\新規作成.xlsx.xlsx"
path = r"C:\Users\1sn311\Desktop\新しいフォルダー (3)\新規 Microsoft Excel ワークシート.xlsx"
workbook = openpyxl.load_workbook(path)
worksheet = workbook.create_sheet(title='新規作成')
# biao1=[]
# biao2=[]

row_n=1
foruda=''
file=''

for root, dirs, fs in os.walk(basedir):

    [dirname, filename] = os.path.split(root)
    # print(dirname)
    # print(filename)
    # print(root)
    foruda=filename

    for filename2 in fs:

        lujing = os.path.join(basedir, filename,filename2)

        text_file = open(lujing, 'r')

        kazo=1
        for line in text_file.readlines():

            if kazo==1 or kazo==2 or kazo==4 or kazo==5:

                line = line.split(',')
                # print(lujing)
                # print(line)
                # os.system('pause')
                kazo+=1

                worksheet.cell(row=row_n, column=1).value = foruda
                worksheet.cell(row=row_n, column=2).value = filename2
                colunm_2=3
                for koumoku in line:

                    worksheet.cell(row=row_n, column=colunm_2).value = koumoku
                    colunm_2+=1
                row_n+=1

            else:

                line = line.split('","')
                # print(lujing)
                # print(line)
                # os.system('pause')
                kazo+=1

                worksheet.cell(row=row_n, column=1).value = foruda
                worksheet.cell(row=row_n, column=2).value = filename2
                colunm_3=3
                for koumoku in line:

                    worksheet.cell(row=row_n, column=colunm_3).value = koumoku
                    colunm_3+=1
                row_n+=1

workbook.save(path)
workbook.close()




