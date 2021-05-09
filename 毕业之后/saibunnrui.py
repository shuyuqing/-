#参考着现有的目录结构，把一堆文件进行分类，然后复制到各自所属的文件夹下面
#因为把文件上传到server上并没有经过分类，所以原有的目录结构就不存在了，所有文件都放到了同一个文件夹下面了
#为了方便比较server上的文件跟本地的文件是否一致，所以要为server上的文件重新建立目录结构
r'''
参考目录: local
                    |-part1
                            |-1
                                |-123.txt
                                |-888.xlsx
                            |-2
                                |-222.txt
                                |-555.xlsx
                    |-part2
                            |-1
                                |-124.txt
                                |-889.xlsx
                            |-2
                            ...
'''

import os;
from shutil import copyfile

aPath=r"C:\Users\a7825\Desktop\我的代码\对应\toridasumatome\local"
#本地的文件夹地址
bPath=r"C:\Users\a7825\Desktop\我的代码\对应\toridasumatome\server"
#server里的文件的文件夹地址
aPath_wenjianjia=os.path.basename(aPath)#获取路径末端文件名
bPath_wenjianjia=os.path.basename(bPath)#获取路径末端文件名

def getAllFiles_a(path):#获取local的所有文件并以相同的方式在server的下建立目录结构

    flist_all = []#完全路径
    flist_wenjian = []#文件名
    for root, dirs, fs in os.walk(path):

        for wenjianjia in dirs:

            ziwenjianjia=os.path.join(root, wenjianjia)#每个文件夹下面的子文件夹
            ziwenjianjia=ziwenjianjia.replace(aPath_wenjianjia,bPath_wenjianjia)#把路径里面的文件夹名换了
            isExists = os.path.exists(ziwenjianjia)#检查文件夹是否存在，存在就跳过，不存在就创建

            # 判断结果
            if not isExists:
                # 如果不存在则创建目录
                # 创建目录操作函数
                os.makedirs(ziwenjianjia)

                print(ziwenjianjia + ' 创建成功')
            else:
                # 如果目录存在则不创建，并提示目录已存在
                print(ziwenjianjia + ' 目录已存在')

        for f in fs:
            f_fullpath = os.path.join(root, f)
            # f_relativepath = f_fullpath[len(path):]#获取文件相对路径
            flist_all.append(f_fullpath)
            flist_wenjian.append(f)

    return flist_all,flist_wenjian

def bunnrui(afiles):#把server文件夹里面的文件进行复制，完成之后就分好类了
    for path in afiles:
        path_new =  path.replace(aPath_wenjianjia,bPath_wenjianjia)
        path_moto = os.path.join(bPath,os.path.basename(path))
        if os.path.exists(path_moto):#判断文件存在,不存在就跳过
            copyfile(path_moto,path_new)#复制文件/从路径中取出末尾文件名

def getAllFiles_b(path):#获取server的所有文件
    flist_all = []#完全路径
    flist_wenjian = []#文件名
    for root, dirs, fs in os.walk(path):
        for f in fs:
            f_fullpath = os.path.join(root, f)
            # f_relativepath = f_fullpath[len(path):]#获取文件相对路径
            flist_all.append(f_fullpath)
            flist_wenjian.append(f)
    return flist_all,flist_wenjian

def dirCompare(apath, bpath):#判断local和server上的文件是否一样
    setA = set(apath)
    setB = set(bpath)
    # 处理仅出现在一个目录中的文件
    onlyFiles = setA ^ setB#对称差集
    onlyInA = []
    onlyInB = []
    for of in onlyFiles:
        if of in apath:
            onlyInA.append(of)
        elif of in bpath:
            onlyInB.append(of)

    if len(onlyInA) > 0:
        print('-' * 20, "only in local",  '-' * 20)
        for of in sorted(onlyInA):
            print(of)

    if len(onlyInB) > 0:
        print('-' * 20, "only in server",  '-' * 20)
        for of in sorted(onlyInB):
            print(of)

if __name__ == '__main__':

    afiles,afiles_wenjian = getAllFiles_a(aPath)
    bfiles,bPath_wenjian = getAllFiles_b(bPath)
    dirCompare(afiles_wenjian,bPath_wenjian)
    bunnrui(afiles)

    print("\ndone!")