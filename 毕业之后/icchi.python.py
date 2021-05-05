
# -*-coding:utf-8-*-

# ===============================================================================
# 目录对比工具(包含子目录 )，并列出
# 1、A比B多了哪些文件
# 2、B比A多了哪些文件
# 3、二者相同的文件: md5比较
# ===============================================================================

import os
import time
import difflib
import hashlib

aPath = r"C:\Users\a7825\Desktop\新建文件夹 (2)\1"
bPath = r"C:\Users\a7825\Desktop\新建文件夹 (2)\2"

#如果aPath下面有某个bPath中所没有的文件夹，这种情况是检测不出来的，所以aPath和bPath中的文件夹的数量和名称要一摸一样才行

def getFileMd5(filename):#把文件流转化为字符串，不相同的两个文件字符串就不一样
    if not os.path.isfile(filename):
        print('file not exist: ' + filename)
        return
    myhash = hashlib.md5()
    f = open(filename, 'rb')
    while True:
        b = f.read(8096)
        if not b:
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()


def getAllFiles(path):
    flist = []
    for root, dirs, fs in os.walk(path):
        for f in fs:
            f_fullpath = os.path.join(root, f)
            f_relativepath = f_fullpath[len(path):]
            flist.append(f_relativepath)
    return flist


def dirCompare(apath, bpath):
    afiles = getAllFiles(apath)
    bfiles = getAllFiles(bpath)

    setA = set(afiles)
    setB = set(bfiles)

    # 转变为set之后就可以求交集，并集和差集了

    commonfiles = setA & setB  # 处理共有文件(求交集)

    for f in sorted(commonfiles):
        amd = getFileMd5(apath + '\\' + f)
        bmd = getFileMd5(bpath + '\\' + f)
        if amd != bmd:
            print("dif file: %s" % (apath + '\\' + f))
            print("dif file: %s" % (bpath + '\\' + f))

    # 处理仅出现在一个目录中的文件
    onlyFiles = setA ^ setB#对称差集
    onlyInA = []
    onlyInB = []
    for of in onlyFiles:
        if of in afiles:
            onlyInA.append(of)
        elif of in bfiles:
            onlyInB.append(of)

    if len(onlyInA) > 0:
        print('-' * 20, "only in ", apath, '-' * 20)
        for of in sorted(onlyInA):
            print(of)

    if len(onlyInB) > 0:
        print('-' * 20, "only in ", bpath, '-' * 20)
        for of in sorted(onlyInB):
            print(of)

if __name__ == '__main__':

    dirCompare(aPath, bPath)
    print("\ndone!")

