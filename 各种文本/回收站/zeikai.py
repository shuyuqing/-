#用来制作正解文列表，之后进行打标签的文本
import csv,sys
#原来csv这个包是可以处理txt文件的
import os,pipei
import openpyxl as op
# file_dir=r"C:\Users\a7825\Desktop\正解文/"
# #原文件的路径
# new_dir1=r"C:\Users\a7825\Desktop\分类L/"
# new_dir2=r"C:\Users\a7825\Desktop\分类R/"

path = r"C:\Users\a7825\Desktop\工作空间\杂物\C005L"
#识别结果

newpath = r"C:\Users\a7825\Desktop\工作空间\杂物\C005L"
#把制作好的正解文列表保存到这里

csv_path = r"C:\Users\a7825\Desktop\工作空间\语音数据\UUDB\第一次实验\打标签"
#正解文

wenjian = r"C005L"
#属于哪个文件

wenjian_1 = r"C005.txt"
#正解文的文件名

path = os.path.join(path,wenjian,'keka')
csv_path = os.path.join(csv_path,wenjian,wenjian_1)
newpath = os.path.join(newpath,wenjian)

str1 = r".wav"
newlist = []
cl_file_path = os.path.join(newpath, 'L.xlsx')

txtwenjian = csv.reader(open(csv_path, 'r', encoding='utf-8'))
b = [i for i in txtwenjian]
b_new = []
zhongzhuan = []

for name in os.listdir(path):
    a = name[6:9]
    zhengjie = b[int(a) - 1]
    #此时的zhengjie是一个list
    zhuanghuan = list(zhengjie[0])
    zhuanghuan.extend('。')
    zhuanghuan = ''.join(zhuanghuan)

    out_file = os.path.join(path,name)
    out_list = pipei.read_out(out_file)

    os.system("pause")
    # # print(b[int(a) - 1])
    # #b[]是正解文
    # newlist.append()
    m = 0
    # print(out_list)
    # print(len(out_list))
    new = list(zhuanghuan)  # zhengjie[0]是一个字符串
    for q in out_list:
        if q[0] == ''or q[0]=='。':
            pass
        else:
            # print(q[0])
            # print(len(q[0]))
            m = m + len(q[0])
            if m<len(new):
                new.insert(m,'/')
                m = m+1
            else:
                print("正解文不够长，我停在了%s这个文件"%name)
                sys.exit();
    if new[-2]!='/':
        new.insert(-1,'/')
        new.remove('/')
        print('%s这个文件需要注意一下,我在最后的句号之前加了一个分隔符'%name)
    xin = ''.join(new)
    zhongzhuan.append(name.replace('.out',''))
    zhongzhuan.append(xin)
    b_new.append(zhongzhuan)
    zhongzhuan = []

wk = op.Workbook()
ws = wk.active

for a in b_new:
    ws.append(a)

wk.save(cl_file_path)



