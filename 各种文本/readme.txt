biaoge:应该是我看pythonABC老师的课试着写出来的东西，我也不太确定啊
convert:把.ad文件先转化为raw文件，然后再转化为wav文件
diyiju:把log文件中第一句话提取出来(也就是识别结果)
panduan:手动把文件分成两类，是在文件yidong的基础上做成的
yidong:在一堆文件中把含有某文件名的文件移动到另一个文件夹里
合并csv文件:把所有的csv文件合并成一个
删除0到391:把CSV文件中前391行都删除掉
handel_info:比较识别结果和正解文，对的话在该特征值第一列加0，错的话在第一列特征值加1
pcm2wav:胡欢文件里发现的未知文本
lstm:推定模型
lstm_dropout:dropout的推定模型
shanchu/shanchu2:把文件名中指定的字符串给删掉
shiyishi:获取文件名并以"."为分隔符分成两部分
chulishuju：删掉特征值数据第一列的“unknown”和最后一列的问号
handel_infov2 (1).py:改进之后的handel_info,可以自由调整帧数对应
handel_info:原版数据打标签的文本，识别结果跟特征值的帧数对应关系只能是识别结果加10再去对应特征值
mfcc:提取mfcc
lianxumfcc:连续提取mfcc
hebing：把几个不同的csv文件和并成一个文件
shangchuhang:删除一个csv文件的头几行和最后几行99
quming:把文件夹里面的文件名都取出来，并写入表格中
lstm_shu - 实验:学习用，自己可以随便乱改的lstm
yupu:可以显示语谱图
fuliye:从Mel-Filter banks中提取传说中的特征值
arrry：连续提取各种特征值的代码
yuchuli.py:把标签和特征值分别提取出来
convert_2:针对pasd这个数据库的wav文件变换
chulishuju2:把开头是"L"或者“R”的句子分别写入不同的文件中(UUDb专用)
example of mlp:用chainer写的mlp的手写识别的例子
pipian:平假名片假名相互转化
zhaocuo:#作用于特征值文件，用于检查打标签的时候第一个空是不是全部被打上了1或者是0
xianshi_1:显示语音文件的各种图像
buroku:只用一个block来进行変調スペクトル分析、得到1ms的数据，为了发表画图，得先把原始的メルフィルタバンク的1到32毫秒的数据先复制出来
xianshi:可以显示spectrogram
xianshi_xi:来自xi的可以显示spectrogram的代码
arufatokatakana:把字母转化为片假名

