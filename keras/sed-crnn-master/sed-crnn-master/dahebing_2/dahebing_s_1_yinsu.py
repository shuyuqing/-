T = True
F = False
import hencyou_1 as he
import shanchongfu as sh
import shanchuhang as sc
import tezhengzhi as te
import zhengjie_RWCP as zR
import os,shutil

import pipei_zhenze_s as pzs
import pipei_zhenze_a as pas
import pipei_s_yinsu as psy
import pipei_s_yinsu_1 as psy1
import pipei_a as pa
import pipei_a_yinsu as pay
import pipei_a_yinsu_1 as pay1

import pipei
import quci_RWCP_SP96 as quci
import balangsu as bl
import qiediao_5 as qie
import muluzai as mu
import pishan as pis
import zhaocuo
import zhengli,zhengli_mizhichuli,zhengli_1
import zhuanyi
import zhengguihua_2 as zheng_2
import zhengguihua as zheng
import  socket
import zuixiao as zx

hostName = socket.gethostname()
print(hostName)

if hostName == 'shu-VAIO':
    path = r'C:\Users\shu\Desktop\gongxiang\symbol_1'  # 批次
    path_beifeng = r'C:\Users\shu\Desktop\gongxiang\数据库'

elif hostName == 'SHU':
    path = r'C:\Users\a7825\Desktop\工作空间\杂物\对比\symbol_1\test'
    path_beifeng = r'C:\Users\a7825\Desktop\工作空间\数据库\test'
    jieweiguanjianzai = 'test'

elif hostName == "symbol2":
    path = r'C:\Users\tsukuba\Desktop\symbol_2'
    path_beifeng = r'C:\Users\tsukuba\Desktop\table'

# path = r'C:\Users\a7825\Desktop\工作空间\杂物\对比\symbol\新建文件夹 (2)'

weidu = 40
chuangkou = 16
#进行正则化的窗口

lintianchong = T
#是否进行零补充
fftwindow = 32
#fft时候的窗口


energy = F
logenergy = T

zhengguihua = F
zhengguihua_2 = F

s1='log'
s2='mizhichuli'
dataname = 'symbol'


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



# pzs.dabiaoqian(path,guanjianzi_1 = s1,guanjianzi_2 = s1+'_'+'biaoqian')#打标签
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



pzs.dabiaoqian(path,guanjianzi_1 = s2,guanjianzi_2 = s2+'_'+'biaoqian')
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


# zhengli.zhengli(path,guanjianzi_1 = s1,guanjianzi_2 = s2,dataname_1 = dataname_1,dataname_2 =dataname_2)#把opentest,closetest,整理出来
# zhengli_mizhichuli.zhengli(path,guanjianzi_2 = s2,dataname_1 = dataname_1,dataname_2=dataname_2)
zhengli_1.zhengli(path,guanjianzi_2 = s2,dataname_1 = dataname_1,dataname_2=dataname_2,guanjianzi_3 = jieweiguanjianzai)
path_1 = os.path.dirname(path)#返回上一层目录
shutil.move(os.path.join(path,dataname_2+'_'+jieweiguanjianzai),path_1)#把整理好的特征值移动到path的上一个目录去


#备份
# shutil.copytree(os.path.join(path),os.path.join(path_beifeng,dataname_2+'_'+jieweiguanjianzi))
# pis.pishan(path,guanjianzi='log',guanjianzi_1 = 'mulu')#批量删除文件夹下的一些东西，注意，第二个关键字根据要删除的是文件（wenjian）还是目录(mulu)来决定
# pis.pishan(path,guanjianzi='log_qian5',guanjianzi_1 = 'mulu')
# pis.pishan(path,guanjianzi='log_yuan',guanjianzi_1 = 'mulu')
# pis.pishan(path,guanjianzi='bulin',guanjianzi_1 = 'mulu')
# pis.pishan(os.path.join(path_beifeng,dataname_2+'_'+jieweiguanjianzi),guanjianzi='wav',guanjianzi_1 = 'mulu')

