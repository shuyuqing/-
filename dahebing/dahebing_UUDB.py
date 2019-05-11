import hencyou as he
import shanchongfu as sh
import shanchuhang as sc
import tezhengzhi as te
import quci_UUDB
import os
import pipei_a_yinsu as pipei
import quci_UUDB as quci
import balangsu as bl
import qiediao_5 as qie5
import qiediao_4 as qie4
import muluzai as mu
import pishan as ps
import zhaocuo
import zhengli,zhuanyi
import zhaocuo
import numpy as np
import suanzhenshu as sz
import zhengguihua as zheng


#注意每次看看标志文件是aglin还是symbol.txt

path = r'C:\Users\a7825\Desktop\工作空间\杂物\对比\ag1'#批次

# sh.shanchongfu_1(path)
#删除不能被识别的wav文件，找出不符合要求的.out文件，并把对应的.out文件跟.wav文件都删除掉
#特别注意：这个删除不能随便乱用，只有当wav文件和.out文件同时在同一个文件夹下才能够使用，如果wav文件和.out文件分开了
#那么所有的wav文件都会被删除掉


# te.tiqu(path)#提取wav文件的特征值




sc.shanchuhang(path)#删除提取特征值的前5行跟后6行



he.hencyou_1(path)#删除文件的前几行，补上零，然后做変調スペクトル的计算
# print("把左右两个声道的正解文都合并一下,然后输入chasen吧")
# os.system("pause")





# quci.qu(path)#生成.ref文件，即正解文文件，生成.log文件，即识别结果
# print("把带有SSSCCC标志的文件都整理好吧")
# os.system("pause")



zheng.zhenggui(path,guanjianzi = 'log')#正则化处理
zheng.zhenggui(path,guanjianzi = 'mizhichuli_log')


pipei.dabiaoqian(path,guanjianzi_1 = 'log_zhengzehua',guanjianzi_2 = 'xinde_log_zhengzehua')#打标签
pipei.dabiaoqian(path,guanjianzi_1 = 'mizhichuli_log',guanjianzi_2 = 'xinde_mizhichuli_zhengzehua')




bl.kongwenjian(path,guanjianzi='xinde_log_zhengzehua')#把大小为0的文件都删除了
bl.kongwenjian(path,guanjianzi='xinde_mizhichuli_zhengzehua')#把大小为0的文件都删除了




bl.pingheng(path,guanjianzi='xinde_log_zhengzehua')#把标签全部是0的文件都移动到桌面去
bl.pingheng(path,guanjianzi='xinde_mizhichuli_zhengzehua')#把标签全部是0的文件都移动到桌面去




bl.pingheng_1(path,guanjianzi='xinde_log_zhengzehua')#把标签全部是1的文件都移动到桌面上去
bl.pingheng_1(path,guanjianzi='xinde_mizhichuli_zhengzehua')#把标签全部是1的文件都移动到桌面去




for wenjian in os.listdir(path):#因为特征值里面0太多了，要切掉一些，这个会把文件切成不同小段

    path_1 = os.path.join(path, wenjian, 'xinde_log_zhengzehua')
    path_new = os.path.join(path, wenjian, 'xinde_log_pingheng_zhengzehua')

    mu.mkdir(path_new)

    for wenjian_1 in os.listdir(path_1):
        path_2 = os.path.join(path_1, wenjian_1)
        qie5.qiexiao(path_2,wenjian_1,path_new)


bl.kongwenjian(path,guanjianzi='xinde_log_pingheng_zhengzehua')#把大小为0的文件都删除了
bl.pingheng(path,guanjianzi = 'xinde_log_pingheng_zhengzehua')#把标签全部是0的文件都移动到桌面去,因为切割之后会留下很多标签全是0的文件




for wenjian in os.listdir(path):#因为特征值里面0太多了，要切掉一些，这个会把文件切成不同小段
    path_1 = os.path.join(path, wenjian, 'xinde_mizhichuli_zhengzehua')
    path_new = os.path.join(path, wenjian, 'xinde_mizhichuli_pingheng_zhengzehua')

    mu.mkdir(path_new)

    for wenjian_1 in os.listdir(path_1):
        path_2 = os.path.join(path_1, wenjian_1)
        qie5.qiexiao(path_2,wenjian_1,path_new)



bl.kongwenjian(path,guanjianzi = 'xinde_mizhichuli_pingheng_zhengzehua')#把大小为0的文件都删除了
bl.pingheng(path,guanjianzi = 'xinde_mizhichuli_pingheng_zhengzehua')#把标签全部是0的文件都移动到桌面去,因为切割之后会留下很多标签全是0的文件




zhengli.zhengli(path,guanjianzi_1='xinde_log_pingheng_zhengzehua',guanjianzi_2 = 'xinde_mizhichuli_pingheng_zhengzehua')#把opentest,closetest,整理出来

# sz.suanzhenshu(path)



# zhaocuo.zhaocuo(path)#作用于特征值文件，用于检查打标签的时候第一个空是不是全部被打上了1或者是0,并且统计标签为1的数据的比重




























# ps.pishan(path,guanjianzi='xinde_log',guanjianzi_1 = 'mulu')#批量删除文件夹下的一些东西，注意，第二个关键字根据要删除的是文件（wenjian）还是目录(mulu)来决定
# ps.pishan(path,guanjianzi='xinde_mizhichuli',guanjianzi_1 = 'mulu')#批量删除文件夹下的一些东西，注意，第二个关键字根据要删除的是文件（wenjian）还是目录(mulu)来决定
# ps.pishan(path,guanjianzi='xinde_log_1',guanjianzi_1 = 'mulu')
# ps.pishan(path,guanjianzi='mizhichuli',guanjianzi_1 = 'mulu')
# ps.pishan(path,guanjianzi='mizhichuli_log',guanjianzi_1 = 'mulu')
# ps.pishan(path,guanjianzi='log_qian5',guanjianzi_1 = 'mulu')
# ps.pishan(path,guanjianzi='log_yuan',guanjianzi_1 = 'mulu')
# ps.pishan(path,guanjianzi='log',guanjianzi_1 = 'mulu')
# ps.pishan(path,guanjianzi='bulin',guanjianzi_1 = 'mulu')
# ps.pishan(path,guanjianzi='xinde_mizhichuli_1',guanjianzi_1 = 'mulu')#批量删除文件夹下的一些东西，注意，第二个关键字根据要删除的是文件（wenjian）还是目录(mulu)来决定
# ps.pishan(path,guanjianzi='qiediao_log',guanjianzi_1 = 'mulu')#批量删除文件夹下的一些东西，注意，第二个关键字根据要删除的是文件（wenjian）还是目录(mulu)来决定
# ps.pishan(path,guanjianzi='qiediao_mizhichuli',guanjianzi_1 = 'mulu')#批量删除文件夹下的一些东西，注意，第二个关键字根据要删除的是文件（wenjian）还是目录(mulu)来决定






# zhuanyi.zhuanyi(path,dizhi_1 = 'qiediao_log',dizhi_2 = 'xinde_log')#把dizhi_1中的文件全部转移到dizhi_2中去,被切割的文件是保存在xinde_log_1中，原文件是留在xinde_log中
# zhuanyi.zhuanyi(path,dizhi_1 = 'qiediao_mizhichuli',dizhi_2 = 'xinde_mizhichuli')#把dizhi_1中的文件全部转移到dizhi_2中去,被切割的文件是保存在xinde_log_1中，原文件是留在xinde_log中



#以下代码为切割文件用的代码

# path_1 = os.path.join(path, 'data','fbank','xuexi')
# path_1_1 = os.path.join(path,'data','mizhichuli','xuexi')
#
# path_new_1 = os.path.join(path, 'data','fbank','xuexi_1')
# path_new_1_1 = os.path.join(path,'data','mizhichuli','xuexi_1')
#
# mu.mkdir(path_new_1)
# mu.mkdir(path_new_1_1)
#
# for wenjian_1 in os.listdir(path_1):
#     path_2 = os.path.join(path_1, wenjian_1)
#     qie5.qiexiao(path_2,wenjian_1,path_new_1)
#
# for wenjian_1_1 in os.listdir(path_1_1):
#     path_2_1 = os.path.join(path_1_1,wenjian_1_1)
#     qie5.qiexiao(path_2_1,wenjian_1_1,path_new_1_1)
#
#
# path_xinde_log = os.path.join(path,'data','fbank','xuexi_1')#把训练数据中大小为0的文件都删掉
# for name_1 in os.listdir(path_xinde_log):
#     path_xinde_log_1 = os.path.join(path_xinde_log,name_1)
#     size = os.path.getsize(path_xinde_log_1)
#     if size <= 2:
#         print("大小为0的文件"+ path_xinde_log_1)
#         os.remove(path_xinde_log_1)
#
# path_xinde_log = os.path.join(path,'data','mizhichuli','xuexi_1')#把训练数据中大小为0的文件都删掉
# for name_1 in os.listdir(path_xinde_log):
#     path_xinde_log_1 = os.path.join(path_xinde_log,name_1)
#     size = os.path.getsize(path_xinde_log_1)
#     if size <= 2:
#         print("大小为0的文件"+ path_xinde_log_1)
#         os.remove(path_xinde_log_1)
#
#
# path_f_closetest = os.path.join(path,'data','fbank','closetest')
# path_f_opentest = os.path.join(path,'data','fbank','opentest')
# path_m_closetest = os.path.join(path,'data','mizhichuli','closetest')
# path_m_opentest = os.path.join(path,'data','mizhichuli','opentest')
#
# mu.mkdir(os.path.join(path,'data','fbank','closetest_1'))
# mu.mkdir(os.path.join(path,'data','fbank','opentest_1'))
# mu.mkdir(os.path.join(path,'data','mizhichuli','closetest_1'))
# mu.mkdir(os.path.join(path,'data','mizhichuli','opentest_1'))
#
#
# for wenjian in os.listdir(path_f_closetest):#对测试数据进行切分
#     path_1 = os.path.join(path_f_closetest,wenjian)
#     path_new_1 = os.path.join(path,'data','fbank','closetest_1')
#     mu.mkdir(path_new_1)
#     # for wenjian_1 in os.listdir(path_1):
#     #     path_2 = os.path.join(path_1, wenjian_1)
#     qie4.qiexiao(path_1,wenjian,path_new_1)
#
# for wenjian in os.listdir(path_f_opentest):#对测试数据进行切分
#     path_1 = os.path.join(path_f_opentest,wenjian)
#     path_new_1 = os.path.join(path,'data','fbank','opentest_1')
#     mu.mkdir(path_new_1)
#     # for wenjian_1 in os.listdir(path_1):
#     #     path_2 = os.path.join(path_1, wenjian_1)
#     qie4.qiexiao(path_1,wenjian,path_new_1)
#
# for wenjian in os.listdir(path_m_opentest):#对测试数据进行切分
#     path_1 = os.path.join(path_m_opentest,wenjian)
#     path_new_1 = os.path.join(path,'data','mizhichuli','opentest_1')
#     mu.mkdir(path_new_1)
#     # for wenjian_1 in os.listdir(path_1):
#     #     path_2 = os.path.join(path_1, wenjian_1)
#     qie4.qiexiao(path_1,wenjian,path_new_1)
#
# for wenjian in os.listdir(path_m_closetest):#对测试数据进行切分
#     path_1 = os.path.join(path_m_closetest,wenjian)
#     path_new_1 = os.path.join(path,'data','mizhichuli','closetest_1')
#     mu.mkdir(path_new_1)
#     # for wenjian_1 in os.listdir(path_1):
#     #     path_2 = os.path.join(path_1, wenjian_1)
#     qie4.qiexiao(path_1,wenjian,path_new_1)
#
#
# liebiao_f_c = os.path.join(path,'data','fbank','closetest_1')#把标签都是0的文件都删除掉
# liebiao_f_o = os.path.join(path,'data','fbank','opentest_1')
# liebiao_m_c = os.path.join(path,'data','mizhichuli','closetest_1')
# liebiao_m_o = os.path.join(path,'data','mizhichuli','opentest_1')
#
#
# for name in os.listdir(liebiao_f_c):
#     path_1 = os.path.join(liebiao_f_c,name)#把标签都是0的文件都删除掉
#     f = open(path_1, 'r')
#     a = np.loadtxt(f, delimiter=',', skiprows=0).astype(np.float32)
#     Labeltrain = a[:, 0:1]
#     f.close()
#     if 1 not in Labeltrain:
#         print("标签全是零的文件" + path_1)
#         os.remove(path_1)
#
# for name in os.listdir(liebiao_f_o):
#     path_1 = os.path.join(liebiao_f_o,name)#把标签都是0的文件都删除掉
#     f = open(path_1, 'r')
#     a = np.loadtxt(f, delimiter=',', skiprows=0).astype(np.float32)
#     Labeltrain = a[:, 0:1]
#     f.close()
#     if 1 not in Labeltrain:
#         print("标签全是零的文件" + path_1)
#         os.remove(path_1)
#
# for name in os.listdir(liebiao_m_o):
#     path_1 = os.path.join(liebiao_m_o,name)#把标签都是0的文件都删除掉
#     f = open(path_1, 'r')
#     a = np.loadtxt(f, delimiter=',', skiprows=0).astype(np.float32)
#     Labeltrain = a[:, 0:1]
#     f.close()
#     if 1 not in Labeltrain:
#         print("标签全是零的文件" + path_1)
#         os.remove(path_1)
#
# for name in os.listdir(liebiao_m_c):
#     path_1 = os.path.join(liebiao_m_c,name)#把标签都是0的文件都删除掉
#     f = open(path_1, 'r')
#     a = np.loadtxt(f, delimiter=',', skiprows=0).astype(np.float32)
#     Labeltrain = a[:, 0:1]
#     f.close()
#     if 1 not in Labeltrain:
#         print("标签全是零的文件" + path_1)
#         os.remove(path_1)














# for wenjian in os.listdir(path):#因为特征值里面0太多了，要切掉一些，这个会把文件切成不同小段
#
#     path_1 = os.path.join(path, wenjian, 'xinde_log')
#     path_new = os.path.join(path, wenjian, '')
#
#     mu.mkdir(path_new)
#
#
#     qie5.qiexiao(path_2,wenjian_1,path_new)
