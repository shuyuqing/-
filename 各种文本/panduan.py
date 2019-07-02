import os, os.path,shutil
import sys

path="C:/Users/a7825/Desktop/学習データ/正确认识/panduan"
newpath="C:/Users/a7825/Desktop/学習データ/正确认识/误-标签为0"
if __name__ == "__main__":
    for x in os.listdir(path):
        fp = os.path.join(path, x)
        print(x)
        str = input("有误认识吗: ")
        if str == 'y':
            #print(fp)

            newfp=os.path.join(newpath,os.path.basename(fp))
            shutil.move(fp,newfp)
            print('移动成功')

        else:
            print('继续')