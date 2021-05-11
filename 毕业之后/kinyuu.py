import win32com.client
import os

rootdir="C:\プロジェクト関係\スキル\ファイル\テスト仕様書\成果"
for i in os.listdir(rootdir):
    xl = win32com.client.Dispatch("Excel.Application")
    xl.Visible = True
    wb=xl.Workbooks.Open(os.path.join(rootdir,i))
    ws=wb.Worksheets(1)
    ws.Cells(6,7).Value="Hello Excel2"
    xl.DisplayAlerts = False
    wb.SaveAs(os.path.join(rootdir,i))
    xl.DisplayAlerts = True
    xl.Quit()