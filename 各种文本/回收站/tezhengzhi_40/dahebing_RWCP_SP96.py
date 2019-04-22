import hencyou as he
import shanchongfu as sh
import shanchuhang as sc
import tezhengzhi as te
import zhengjie_RWCP as zR

path = r'C:\Users\a7825\Desktop\工作空间\杂物\对比'#批次

# sh.shanchongfu_1(path)#删除不能被识别的wav文件，找出不符合要求的.out文件，并把对应的.out文件跟.wav文件都删除掉
# zR.zhengjie(path)#在正解文的最后加上句号，然后提取出需要的正解文
te.tiqu(path)#提取wav文件的特征值
sc.shanchuhang(path)#删除提取特征值的前5行跟后6行
he.hencyou_1(path)#删除文件的前5行，补上零，然后做変調スペクトル的计算（原料是刚提取出来的特征值。做计算的时候只要删除前几行即可，后面的几行保留，不删除。）
# print("把左右两个声道的正解文都合并一下,然后输入chasen吧")
# os.system("pause")
#
# quci.qu(path)#生成.ref文件，即正解文文件，生成.log文件，即识别结果

# print("把带有SSSCCC标志的文件都整理好吧")
# os.system("pause")

# pipei_5.dabiaoqian(path)#给fbank打标签
# pipei_6.dabiaoqian(path)#给mizhichuli打标签
# pipei_8.dabiaoqian(path)

# import zhengli
# zhengli.zhengli(path)#把opentest,closetest,整理出来
# #
# import zhaocuo
# zhaocuo.zhaocuo(path)#作用于特征值文件，用于检查打标签的时候第一个空是不是全部被打上了1或者是0,并且统计标签为1的数据的比重


