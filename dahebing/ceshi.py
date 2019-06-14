import shutil,os

path = r'C:\Users\a7825\Desktop\新しいフォルダー\新建文件夹'
path_2 =r'C:\Users\a7825\Desktop\新しいフォルダー\新建文件夹1\移动'
path_1 = os.path.dirname(path)

print(path_1)

if os.path.exists(os.path.join(path_1,'移动')):  # 把文件名从路径中剥离出来，如果早已存在，就把它删除了，再覆盖掉

    os.remove(os.path.join(path_1,'移动'))
    shutil.move(path_2, path_1)

else:
    shutil.move(path_2, path_1)

# shutil.move(r'C:\Users\a7825\Desktop\新しいフォルダー\新建文件夹1\移动',path_1)
shutil.copytree(r"C:\Users\a7825\Desktop\新しいフォルダー\新建文件夹1",r"C:\Users\a7825\Desktop\新建文件夹")