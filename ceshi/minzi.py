import os

filename = r'C:\Users\a7825\Desktop\新建文件夹\新建文件夹\C064L/C064.txt'
(filepath,tempfilename) = os.path.split(filename);
(shotname,extension) = os.path.splitext(filename);

print(filepath)
# print(tempfilename)
# print(shotname)
# print(extension)