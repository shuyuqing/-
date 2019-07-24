T = True
F = False
import hencyou_1 as he
import shanchongfu as sh
import shanchuhang as sc
import tezhengzhi as te
import zhengjie_RWCP as zR
import os,shutil

import pipei_s as ps
import pipei_s_yinsu as psy
import pipei_s_yinsu_1 as psy1
import pipei_zhenze_a as pza
import pipei_zhenze_s as pzs
import pipei_a_yinsu as pay
import pipei_a_yinsu_1 as pay1

import pipei
import quci_RWCP_SP96 as quci
import balangsu as bl
import qiediao_5 as qie
import muluzai as mu
import pishan as pis
import zhaocuo
import zhengli,zhuanyi
import zhengguihua_2 as zheng_2
import zhengguihua as zheng
import  socket
import zuixiao as zx
import zhengli_mizhichuli,zhengli_1

hostName = socket.gethostname()
print(hostName)

if hostName == 'shu-VAIO':
    path = r'C:\Users\shu\Desktop\gongxiang\ag1_1\test'  # 批次
    path_beifeng = r'C:\Users\shu\Desktop\gongxiang\数据库\test'
    jieweiguanjianzi = 'test'

elif hostName == 'SHU':
    path = r'C:\Users\a7825\Desktop\工作空间\杂物\对比\ag1_1'
    path_beifeng = r'G:\研究生二年级\数据库'

elif hostName == "ag12":
    path = r'C:\Users\a7825\OneDrive\デスクトップ\ag1_2'
    path_beifeng = r'C:\Users\a7825\OneDrive\デスクトップ\table'


weidu = 40
chuangkou = 8
#进行正则化的窗口

lintianchong = T
#是否进行零补充
fftwindow = 8
#fft时候的窗口


energy = F
logenergy = T

zhengguihua = F
zhengguihua_2 = F

s1='log'
s2='mizhichuli'
dataname = 'ag1_1'


if lintianchong == True:

    padding = fftwindow - chuangkou#需要填充的0的数量
else:
    padding = 0

# sh.shanchongfu_1(path)
# #删除不能被识别的wav文件，找出不符合要求的.out文件，并把对应的.out文件跟.wav文件都删除掉
#特别注意：这个删除不能随便乱用，只有当wav文件和.out文件同时在同一个文件夹下才能够使用，如果wav文件和.out文件分开了
#那么所有的wav文件都会被删除掉



# zR.zhengjie(path)#在正解文的最后加上句号，然后提取出需要的正解文

pis.pishan(path,guanjianzi='log_biaoqian',guanjianzi_1 = 'mulu')#批量删除文件夹下的一些东西，注意，第二个关键字根据要删除的是文件（wenjian）还是目录(mulu)来决定
pis.pishan(path,guanjianzi='log_biaoqian_pingheng',guanjianzi_1 = 'mulu')
pis.pishan(path,guanjianzi='mizhichuli',guanjianzi_1 = 'mulu')
pis.pishan(path,guanjianzi='mizhichuli_biaoqian_pingheng',guanjianzi_1 = 'mulu')
pis.pishan(path,guanjianzi='mizhichuli_biaoqian',guanjianzi_1 = 'mulu')


te.tiqu(path,weidu,logenergy,energy)#提取wav文件的特征值

dataname = dataname +'_'+ str(weidu)

sc.shanchuhang(path)#删除提取特征值的前5行跟后6行


he.hencyou_1(path,chuangkou,padding,lintianchong)#删除文件的前几行，补上零，然后做変調スペクトル的计算

dataname = dataname +'_'+ str(chuangkou)+ '_'+str(fftwindow)
dataname_1 = dataname_2 = dataname


# print("把左右两个声道的正解文都合并一下,然后输入chasen吧")
# os.system("pause")




#quci.qu(path)#生成.ref文件，即正解文文件，生成.log文件，即识别结果
# print("把带有SSSCCC标志的文件都整理好吧")
# os.system("pause")


if zhengguihua == True:
    # zheng.zhenggui(path,guanjianzi = s1)#正则化处理
    # zheng.zhenggui(path,guanjianzi = s2)

    s1 = s1 + '_' + 'zhengguihua'
    s2 = s2 + '_' + 'zhengguihua'

    dataname_1 = dataname_1 + '_' + 'zhengguihua_2'
    dataname_2 = dataname_2 + '_' + 'zhengguihua_2'



if zhengguihua_2 == True:
    # zheng_2.zhenggui(path,guanjianzi = s1,guanjianzi_1='zhengguihua_2')#正则化处理
    # zheng_2.zhenggui(path,guanjianzi = s2,guanjianzi_1='zhengguihua_2')

    s1 = s1 + '_' + 'zhengguihua_2'
    s2 = s2 + '_' + 'zhengguihua_2'

    dataname_1 = dataname_1 + '_' + 'zhengguihua_2'
    dataname_2 = dataname_2 + '_' + 'zhengguihua_2'



# pza.dabiaoqian(path,guanjianzi_1 = s1,guanjianzi_2 = s1+'_'+'biaoqian')#打标签
# zx.zuixiao(path,guanjianzi=s1+'_'+'biaoqian',xiaxian=10)
# bl.kongwenjian(path,guanjianzi=s1+'_'+'biaoqian')#把大小为0的文件都删除了
# bl.pingheng_2(path,guanjianzi= s1+'_'+'biaoqian')#把标签全部是0的文件都移动到桌面去
# bl.pingheng_3(path,guanjianzi=s1+'_'+'biaoqian')#把标签全部是1的文件都移动到桌面上去
s1 = s1+'_'+'biaoqian'
dataname_1 = dataname_1 + '_' + 'biaoqian'


# for wenjian in os.listdir(path):#因为特征值里面0太多了，要切掉一些，这个会把文件切成不同小段
#     path_1 = os.path.join(path, wenjian, s1)
#     path_new = os.path.join(path, wenjian, s1+'_'+'pingheng')
#     mu.mkdir(path_new)
#     for wenjian_1 in os.listdir(path_1):
#         path_2 = os.path.join(path_1, wenjian_1)
#         qie.qiexiao(path_2,wenjian_1,path_new)
# bl.pingheng_2(path, guanjianzi=s1+'_'+'pingheng')  # 把标签全部是0的文件都移动到桌面去,因为切割之后会留下很多标签全是0的文件
# zx.zuixiao(path,guanjianzi=s1+'_'+'pingheng',xiaxian=10)

s1 = s1+'_'+'pingheng'
dataname_1 = dataname_1 + '_' + 'pingheng'






pza.dabiaoqian(path,guanjianzi_1 = s2,guanjianzi_2 = s2+'_'+'biaoqian')
zx.zuixiao(path,guanjianzi=s2+'_'+'biaoqian',xiaxian=10)
bl.kongwenjian(path,guanjianzi=s2+'_'+'biaoqian')#把大小为0的文件都删除了
bl.pingheng_2(path,guanjianzi= s2+'_'+'biaoqian')#把标签全部是0的文件都移动到桌面去
bl.pingheng_3(path,guanjianzi=s2+'_'+'biaoqian')#把标签全部是1的文件都移动到桌面去
s2 = s2+'_'+'biaoqian'
dataname_2 = dataname_2 + '_' + 'biaoqian'


for wenjian in os.listdir(path):#因为特征值里面0太多了，要切掉一些，这个会把文件切成不同小段
    path_1 = os.path.join(path, wenjian, s2)
    path_new = os.path.join(path, wenjian, s2+'_'+'pingheng')
    mu.mkdir(path_new)
    for wenjian_1 in os.listdir(path_1):
        path_2 = os.path.join(path_1, wenjian_1)
        qie.qiexiao(path_2,wenjian_1,path_new)
bl.pingheng_2(path,guanjianzi = s2+'_'+'pingheng')#把标签全部是0的文件都移动到桌面去,因为切割之后会留下很多标签全是0的文件
zx.zuixiao(path,guanjianzi=s2+'_'+'pingheng',xiaxian=10)

s2 = s2+'_'+'pingheng'
dataname_2 = dataname_2 + '_' + 'pingheng'

zhengli_1.zhengli(path,guanjianzi_2 = s2,dataname_1 = dataname_1,dataname_2=dataname_2,guanjianzi_3 = jieweiguanjianzi)

path_1 = os.path.dirname(path)
shutil.move(os.path.join(path,dataname_2),path_1)
shutil.copytree(os.path.join(path),os.path.join(path_beifeng,dataname_2))

pis.pishan(path,guanjianzi='log',guanjianzi_1 = 'mulu')#批量删除文件夹下的一些东西，注意，第二个关键字根据要删除的是文件（wenjian）还是目录(mulu)来决定
pis.pishan(path,guanjianzi='log_qian5',guanjianzi_1 = 'mulu')
pis.pishan(path,guanjianzi='log_yuan',guanjianzi_1 = 'mulu')
pis.pishan(path,guanjianzi='bulin',guanjianzi_1 = 'mulu')

pis.pishan(os.path.join(path_beifeng,dataname_2),guanjianzi='wav',guanjianzi_1 = 'mulu')

# zhaocuo.zhaocuo(path)#作用于特征值文件，用于检查打标签的时候第一个空是不是全部被打上了1�
