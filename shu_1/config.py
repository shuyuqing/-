#!/usr/bin/env python
# -*- coding: utf-8 -*-
T = True
N = None

gakusyu = r'/home/users/y.shu/data5/fbank/xuexi'

#所有的学习数据

opentest = r'/home/users/y.shu/data5/fbank/opentest'
#opentest的数据

closetest = r'/home/users/y.shu/data5/fbank/closetest'
#closetest的数据

mse = N
cross = T
#选择用哪个损失函数,注意，只能有一个选T,其它的全部选N

inputN = 25
outputN = 2
#输入到神经网络的数据的次元以及输出的个数

batchsize = 10
epoch = 100
gpu = 1
save = T
lr = 0.00032#学习率

open_model ="1model"
close_model ="59model"
#opentest以及closetest所调用的模型

xunlian = T
#训练开关

bice = N
bice_lianxu = T
#closetest的按钮

kaice = T
kaice_lianxu = T
#opentest的开关

lstmcenshu = 4
#lstm的层数

dropout = 0

adagrad_lr = 0.0001
#学习率的衰减参数

embed_size = 220
#embed层的数量

test_size = 100
#想连续测试几个模型

cudnn = T
#是否使用cudnn


