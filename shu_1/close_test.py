#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,os,label
from chainer import cuda, optimizers, serializers,Variable
from model_cross import BLSTM #3norm, 4midlelayer, 5Thres
from libs.base import App as AbstractApp, Logger as Log
import numpy as np
import config as cfg
from sklearn.metrics import confusion_matrix


def test(model_file,moderu):
    # Load files

    Log.v('')
    Log.v("initialize ...")
    Log.v('')

    # Set up a neural network

    Log.i("loading a model from %s ..." % model_file)
    serializers.load_npz(model_file, moderu)

    # Set closetest data
    preds = 0.0
    cishu = 0
    loss_1 = 0.0

    pathDir = os.listdir(cfg.closetest)

    yucezhi_1 = []
    zhenzhi_1 = []

    # losslist = []
    # fause_ratelist= []
    # correct_ratelist = []
    # correct_flist = []
    # fause_flist = []


    for allDir in pathDir:#测试数据是一个一个地往模型里扔
        print(allDir)
        filename = allDir
        allDir = os.path.join(cfg.closetest, allDir)
        f = open(allDir, 'r')
        a = np.loadtxt(f, delimiter=',', skiprows=0, ).astype(np.float32)
        # print(a.shape)
        closetestX = a[:, 1:None]
        closetestlabel = a[:, 0:1]
        # print('Xclosetest shape: {}'.format(closetestX.shape))

        if cfg.mse == True:

            closetestlabel = label.label_1(closetestlabel)

        if cfg.cross == True:

            closetestlabel = label.label_2(closetestlabel)

        # print('Yclosetest shape: {}'.format(closetestlabel.shape))
        # skl.preprocessing.normalize(closetestX, norm='l2')

        zhuanghuan =[]
        zhuanghuan1 =[]
        #输入到blsm中的数据必须是二维的array,形如[[1 2]]，第一个维度表示数据的个数，第二个维度是具体的特征值

        zhuanghuan.append(np.array(closetestX,np.float32))
        zhuanghuan1.append(np.array(closetestlabel,np.int32))
        closetestX = np.array(zhuanghuan)
        closetestlabel = np.array(zhuanghuan1)

        testloss, preds_1, yucezhi= moderu(closetestX, closetestlabel)

        # print("现在输出预测值")
        # print("现在输出preds_1")
        # print(preds_1)
        # print("现在输出closetestlabel")
        # print(closetestlabel)
        # os.system("pause")
        yucezhi_1.extend(yucezhi)
        zhenzhi_1.extend(closetestlabel)

        loss_1 = loss_1 + testloss
        preds += preds_1
        cishu = cishu+1
        # print(preds)
        # print(cishu)
        testloss.unchain_backward()

    yucezhi_2 = []
    zhenzhi_2 = []

    for a in zhenzhi_1:
        # print(type(a))
        # os.system("pause")
        zhenzhi_2.extend(a.tolist())

    for b in yucezhi_1:
        # print(type(b.data))
        # os.system("pause")
        yucezhi_2.extend((b.data).tolist())  # 加了tolist居然好使了
    confuse = confusion_matrix(zhenzhi_2, yucezhi_2)

    Log.i("#closetest:----datasize: %d, accuracy: %f, testloss: %f"% (cishu, preds/cishu, loss_1.data/cishu))

    # losslist.append(testloss/cishu)

    Log.i("the confuse matrix is")
    Log.i(confuse)

    '''
       混淆矩阵的形状是
                   预测值
                   0   1
       真实值  0   a   b
               1   c   d
       真实值是0，预测值也是0的情况是有a次
       真实值是0，但是预测值是1的情况有b次。。。。。。
    '''
    print('the name of model is%s'%model_file)
    Log.i('the name of model is%s'%model_file)
    print('这次测试的混淆矩阵是')
    print(confuse)#输入混淆矩阵的是两个list
    fause = confuse[1][1] / (confuse[1][0] + confuse[1][1])
    fause_1 = confuse[1][1] / (confuse[0][1] + confuse[1][1])
    correct = confuse[0][0] / (confuse[0][0] + confuse[0][1])
    correct_1 = confuse[0][0] / (confuse[0][0] + confuse[1][0])
    c = confuse[0][0] + confuse[0][1]
    f = confuse[1][0] + confuse[1][1]
    all = confuse[0][0] + confuse[0][1] + confuse[1][0] + confuse[1][1]
    fause_rate = f / all
    correct_rate = c / all
    correct_f = (2 * correct * correct_1) / (correct + correct_1)
    fause_f = (2 * fause * fause_1) / (fause + fause_1)

    # print("测试loss是")
    # print(testloss)
    # os.system("pause")


    print("总共的帧数是:%d"%all)
    Log.i("all of the frames:%d"%all)
    print("错误识别的再现率是：%f"%fause)
    Log.i("the precision of label1:%f"%float(fause))
    # fause_ratelist.append(fause)

    print("原本就是错误的帧数为:%f,占总帧数的%f"%(f,fause_rate))
    Log.i("the number of label1:%f,label1's rate%f"%(f,fause_rate))
    print("正确认识的再现率是:%f"%correct)
    Log.i("the precision of label0:%f"%float(correct))
    # correct_ratelist.append(correct)

    print("原本就是正确的帧数为:%f,占总帧数的%f"%(c,correct_rate))
    Log.i("the number of label0:%f,label0's rate%f"%(c,correct_rate))
    print("错误识别的适合率是：%f" % fause_1)
    Log.i("the recall of label1:%f"%fause_1)
    print("正确认识的适合率是：%f" % correct_1)
    Log.i("the recall of label0:%f"%correct_1)
    print("正确认识的F值为:%f" % correct_f)
    # correct_flist.append(correct_f)

    Log.i("the F score of label0:%f"%correct_f)
    print("错误识别的F值为：%f" % fause_f)
    # fause_flist.append(fause_f)

    Log.i("the F score of label1:%f"%fause_f)

    return loss_1.data/cishu,fause,fause_f,correct_rate,correct_f,preds/cishu
    print('##################### ClosePredict Done ########################')