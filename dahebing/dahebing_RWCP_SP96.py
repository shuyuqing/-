T = True
F = False
import hencyou as he
import shanchongfu as sh
import shanchuhang as sc
import tezhengzhi as te
import zhengjie_RWCP as zR
import os

import pipei_s as ps
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
import zhengli,zhuanyi
import zhengguihua_2 as zheng_2
import zhengguihua as zheng


path = r'C:\Users\a7825\Desktop\工作空间\杂物\对比\symbol'#批次


weidu = 24
chuangkou = 32
zhengguihua = F
zhengguihua_2 = T



# sh.shanchongfu_1(path)
# #删除不能被识别的wav文件，找出不符合要求的.out文件，并把对应的.out文件跟.wav文件都删除掉
#特别注意：这个删除不能随便乱用，只有当wav文件和.out文件同时在同一个文件夹下才能够使用，如果wav文件和.out文件分开了
#那么所有的wav文件都会被删除掉



# zR.zhengjie(path)#在正解文的最后加上句号，然后提取出需要的正解文



# te.tiqu(path,weidu)#提取wav文件的特征值
# sc.shanchuhang(path)#删除提取特征值的前5行跟后6行




# he.hencyou_1(path,chuangkou)#删除文件的前几行，补上零，然后做変調スペクトル的计算
# print("把左右两个声道的正解文都合并一下,然后输入chasen吧")
# os.system("pause")




#quci.qu(path)#生成.ref文件，即正解文文件，生成.log文件，即识别结果
# print("把带有SSSCCC标志的文件都整理好吧")
# os.system("pause")


s1='log'
s1_1='log_biaoqian'
s2='mizhichuli'
s2_1='mizhichuli_biaoqian'



if zhengguihua == True:
    zheng.zhenggui(path,guanjianzi = s1)#正则化处理
    zheng.zhenggui(path,guanjianzi = s2)
    s1 = 'log_zhengguihua'
    s1_1 = 'log_zhengguihua_biaoqian'
    s2 = 'mizhichuli_zhengguihua'
    s2_1 = 'mizhichuli_zhengguihua_biaoqian'


if zhengguihua_2 == True:
    zheng_2.zhenggui(path,guanjianzi = s1,guanjianzi_1='zhengguihua_2')#正则化处理
    zheng_2.zhenggui(path,guanjianzi = s2,guanjianzi_1='zhengguihua_2')
    s1 = 'log_zhengguihua_2'
    s1_1 = 'log_zhengguihua_2_biaoqian'
    s2 = 'mizhichuli_zhengguihua_2'
    s2_1 = 'mizhichuli_zhengguihua_2_biaoqian'


print(s1)
os.system('pause')

pa.dabiaoqian(path,guanjianzi_1 = s1,guanjianzi_2 = s1_1)#打标签
bl.kongwenjian(path,guanjianzi=s1_1)#把大小为0的文件都删除了
bl.pingheng(path,guanjianzi= s1_1)#把标签全部是0的文件都移动到桌面去
bl.pingheng_1(path,guanjianzi=s1_1)#把标签全部是1的文件都移动到桌面上去


pa.dabiaoqian(path,guanjianzi_1 = s2,guanjianzi_2 = s2_1)
bl.kongwenjian(path,guanjianzi=s2_1)#把大小为0的文件都删除了
bl.pingheng(path,guanjianzi= s2_1)#把标签全部是0的文件都移动到桌面去
bl.pingheng_1(path,guanjianzi=s2_1)#把标签全部是1的文件都移动到桌面去



s1_1_1 = s1_1+'_pinghen'
for wenjian in os.listdir(path):#因为特征值里面0太多了，要切掉一些，这个会把文件切成不同小段
    path_1 = os.path.join(path, wenjian, s1_1)
    path_new = os.path.join(path, wenjian, s1_1_1)
    mu.mkdir(path_new)
    for wenjian_1 in os.listdir(path_1):
        path_2 = os.path.join(path_1, wenjian_1)
        qie.qiexiao(path_2,wenjian_1,path_new)
bl.pingheng(path,guanjianzi = s1_1_1)#把标签全部是0的文件都移动到桌面去,因为切割之后会留下很多标签全是0的文件




s2_1_1 = s2_1 + '_pinghen'
for wenjian in os.listdir(path):#因为特征值里面0太多了，要切掉一些，这个会把文件切成不同小段
    path_1 = os.path.join(path, wenjian, s2_1)
    path_new = os.path.join(path, wenjian, s2_1_1)
    mu.mkdir(path_new)
    for wenjian_1 in os.listdir(path_1):
        path_2 = os.path.join(path_1, wenjian_1)
        qie.qiexiao(path_2,wenjian_1,path_new)
bl.pingheng(path,guanjianzi = s2_1_1)#把标签全部是0的文件都移动到桌面去,因为切割之后会留下很多标签全是0的文件




zhengli.zhengli(path,guanjianzi_1 = s1_1_1,guanjianzi_2 = s2_1_1)#把opentest,closetest,整理出来






# zhaocuo.zhaocuo(path)#作用于特征值文件，用于检查打标签的时候第一个空是不是全部被打上了1或者是0,并且统计标签为1的数据的比重





















pis.pishan(path,guanjianzi='log_zhengguihua_1',guanjianzi_1 = 'mulu')#批量删除文件夹下的一些东西，注意，第二个关键字根据要删除的是文件（wenjian）还是目录(mulu)来决定
pis.pishan(path,guanjianzi='mizhichuli_biaoqian',guanjianzi_1 = 'mulu')#批量删除文件夹下的一些东西，注意，第二个关键字根据要删除的是文件（wenjian）还是目录(mulu)来决定
pis.pishan(path,guanjianzi='mizhichuli_biaoqian_pinghen',guanjianzi_1 = 'mulu')
pis.pishan(path,guanjianzi='mizhichuli_zhengguihua_1',guanjianzi_1 = 'mulu')
pis.pishan(path,guanjianzi='log_biaoqian_pinghen',guanjianzi_1 = 'mulu')
pis.pishan(path,guanjianzi='log_biaoqian',guanjianzi_1 = 'mulu')



# zhuanyi.zhuanyi(path,dizhi_1 = 'qiediao_log',dizhi_2 = 'xinde_log')#把dizhi_1中的文件全部转移到dizhi_2中去,被切割的文件是保存在xinde_log_1中，原文件是留在xinde_log中
# zhuanyi.zhuanyi(path,dizhi_1 = 'qiediao_mizhichuli',dizhi_2 = 'xinde_mizhichuli')#把dizhi_1中的文件全部转移到dizhi_2中去,被切割的文件是保存在xinde_log_1中，原文件是留在xinde_log中