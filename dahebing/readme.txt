dahebing_RWCP_SP96:RWCP_SP96专用的，从mmfs27中获得识别结果之后，到标签全部被打上去的一整个过程
dahebing_UUDB:UUDB专用
xinlaidu:使用信赖度来判断是否出现错误识别ベースラインシステム
pipei_a:在单词单位上打标签(scoring文件是align1)
pipei_a_yinsu:在音素单位上打标签(scoring文件是align1),识别结果和正解单词比较的时候要转化为音素去比较
pipei_a_yinsu_1:在音素单位上打标签(scoring文件是align1),识别结果和正解单词比较的时候直接比较汉字
pipei_s:在单词单位上打标签(scoring文件是symbol.txt)
pipei_s_yinsu:在音素单位上打标签(scoring文件是symbol.txt),识别结果和正解单词比较的时候要转化为音素去比较
pipei_s_yinsu_1:在音素单位上打标签(scoring文件是symbol.txt),识别结果和正解单词比较的时候直接比较汉字


以下是用来提取特征值,计算変調スペクトル,整理学习数据
zhengjie_RWCP:先给正解文加句号，(合并了jiajuhao)然后把RWCP的正解文提取出来，RWCP专用
zhengli:把得到的fbank和変調スペクトル按all，opentest，closetest,xuexi整理出来
chawenjian:检查.out文件是否会出现空文件，或者是识别结果只有一个句号,然后检查这个文件夹下wav文件跟.out文件的数量是否相同,然后把费了的文件都删除掉
dianlog_RWCP_SP96:RWCP_SP96专用的,根据原有的.out文件生成能被scoring所识别的标准日志文件(.log文件)
fuliye_gai:计算変調スペクトル
hencyou:#删除fbank的前五行，再在后面补零，再做変調スペクトル的计算
jiajuhao:#如果一行的末尾没有句号就加上一个句号。删除句子中的.,把，都改成、这个是RWCP专用的
quci:#用于从chasen出力文件中取出已经分割好了的单词，生成.ref文件（正解文）和日志文件(.log文件)
shanchongfu:把未能被julius识别的音频文件都删除掉,julius认识之后，把全部.out文件都挑出来
shanchuhang:删除一个文件中的前几行跟后面几行
shanchuhang_2:#删除メルフィルタバンク特征值文件中的前几行跟后面几行（被打上标签“9”的那几行特征值）
shangchuhang_qian5:#为了计算変調スペクトル，把提取出来的fbank的前5帧删了
tezhengzhi:提取各种特征值
zhaocuo:#作用于特征值文件，用于检查打标签的时候第一个空是不是全部被打上了1或者是0，并且统计标签为1的数据的比重
balangsu:#把大小为0的文件都删掉,而且把标签全部是0,全是1的文件都移动到桌面去。原料是打好标签的特征值
qiediao_5:#把特征值文件切成只由一段1和一段0组成的，一段一段的文件
suanzhenshu:计算一批数据的最长帧数，平均帧数以及最短帧数
zhengguihua:把学习数据正规化(沿着时间轴做)
zhengguihua_1:把学习数据正规化(沿着周期轴做)

其他
make_kana_convertor:#可以把英语字母转化为片假名
muluzai:自动创建新的目录
pipei:#用正则匹配找出认识结果的帧数表的文本
pipei_8:#用于打标签，解决socring把两个单词合并成一个单词的问题,给特征值打标签
strQ2B:把字符串全角转半角
chongzao:#用于在解析出来的.out文件中加上CCCSSS的标志，解决socring把两个单词合并成一个单词的问题
pishan:批量删除文件夹下的文件夹以及文件
zhuanyi:把一个文件夹下的文件都剪切，粘贴到另外一个文件夹下
tongji:把一批文件中的所有特征值文件的个数统计出来

废弃物
zidian:为打标签而建立三个字典
qiediao_4:#用于把标签0比较多的文件切成小段。


