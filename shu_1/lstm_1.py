#!/usr/bin/env python
# -*- coding: utf-8 -*-
#用的chainer版本是1.24
#注意，关于入力数据，要先把array塞入list,然后再把list变成array
import sys,os,label
import trainer as tr
from libs.base import App as AbstractApp, Logger as Log
import numpy as np
import config as cfg
import close_test as ct
import open_test as ot
import config as cfg
from model_cross import BLSTM #3norm, 4midlelayer, 5Thres
from chainer import cuda

np.random.seed(1515)

class App(AbstractApp):

    def _initialize(self):
        # self._logdir = self._basedir + '/../logs'
        self._def_arg('--batchsize', '-b', type=int, default=cfg.batchsize,
                      help='Number of examples in each mini-batch')
        self._def_arg('--epoch', '-e', type=int, default=cfg.epoch,
                      help='Number of sweeps over the dataset to train')
        self._def_arg('--gpu', '-g', type=int, default=cfg.gpu,
                      help='GPU ID (negative value indicates CPU)')
        self._def_arg('--save', action='store_true', default=cfg.save,
                      help='Save the NN model')

    def main(self):

        if cfg.xunlian == True:

            Log.i("*** [START] ***")
            Log.i(" ")
            Log.i(" ")

            tr.train(
                n_epoch=self._args.epoch,
                batch_size=self._args.batchsize,
                gpu=self._args.gpu,
                save=self._args.save
                # 要不要保存训练好的模型
                # save="kakilstm.model" if self._args.save else None,
            )

        if cfg.bice == True:

            Log.i("*** [closetesting] ***")
            Log.i(" ")
            Log.i(" ")

            losslist = []
            fause_ratelist = []
            correct_ratelist = []
            correct_flist = []
            fause_flist = []
            accuracy = []

            cls = BLSTM
            model = cls(
                f_dim=cfg.inputN,
                n_labels=cfg.outputN,  # (11*2)+1,
                dropout=0,
                train=False,
            )

            if cfg.gpu >= 0:
                cuda.get_device_from_id(cfg.gpu)
                model.to_gpu()
                # cuda.get_device_from_id(gpu)
                # model.to_gpu()

            if cfg.bice_lianxu == True:

                for i in range(cfg.test_size):
                    testloss,fause_rate,fause_f,correct_rate,correct_f, matomeaccu= ct.test(model_file = os.path.join(os.getcwd()+'/model/'+str(i + 1) + 'model'), moderu =model)  # 执行closetest,连续测试各个模型

                    losslist.append(testloss)
                    fause_ratelist.append(fause_rate)
                    correct_ratelist.append(correct_rate)
                    correct_flist.append(correct_f)
                    fause_flist.append(fause_f)
                    accuracy.append(matomeaccu)
            else:
                testloss, fause_rate, fause_f, correct_rate, correct_f, matomeaccu = ct.test(model_file=cfg.close_model,moderu =model)  # 执行closetest,只测试一个模型

                losslist.append(testloss)
                fause_ratelist.append(fause_rate)
                correct_ratelist.append(correct_rate)
                correct_flist.append(correct_f)
                fause_flist.append(fause_f)
                accuracy.append(matomeaccu)

            np.savetxt(os.getcwd() + '/libs/closetest/loss.txt', losslist)  # 把loss存入文件中
            np.savetxt(os.getcwd() + '/libs/closetest/fause_rate.txt', fause_ratelist)
            np.savetxt(os.getcwd() + '/libs/closetest/correct_rate.txt', correct_ratelist)
            np.savetxt(os.getcwd() + '/libs/closetest/correct_f.txt', correct_flist)
            np.savetxt(os.getcwd() + '/libs/closetest/fause_f.txt', fause_flist)
            np.savetxt(os.getcwd() + '/libs/closetest/accuracy.txt', accuracy)

            Log.i("*** [CLOSETESTDONE] ***")
            Log.i(" ")
            Log.i(" ")

        if cfg.kaice == True:

            Log.i("*** [opentesting] ***")
            Log.i(" ")
            Log.i(" ")

            losslist = []
            fause_ratelist= []
            correct_ratelist = []
            correct_flist = []
            fause_flist = []
            accuracy = []

            cls = BLSTM
            model_1 = cls(
                f_dim=cfg.inputN,
                n_labels=cfg.outputN,  # (11*2)+1,
                dropout=0,
                train=False,
            )

            if cfg.gpu >= 0:
                cuda.get_device_from_id(cfg.gpu)
                model_1.to_gpu()
                # cuda.get_device_from_id(gpu)
                # model.to_gpu()

            if cfg.kaice_lianxu == True:

                for i in range(cfg.test_size):
                    testloss, fause_rate, fause_f, correct_rate, correct_f,matomeaccu = ot.test(model_file=os.path.join(os.getcwd()+'/model/'+str(i + 1) + 'model'), moderu = model_1) # 执行closetest,连续测试各个模型

                    losslist.append(testloss)
                    fause_ratelist.append(fause_rate)
                    correct_ratelist.append(correct_rate)
                    correct_flist.append(correct_f)
                    fause_flist.append(fause_f)
                    accuracy.append(matomeaccu)
            else:
                testloss, fause_rate, fause_f, correct_rate, correct_f, matomeaccu = ot.test(model_file=cfg.open_model,moderu = model_1)  # 执行closetest,只测试一个模型

                losslist.append(testloss)
                fause_ratelist.append(fause_rate)
                correct_ratelist.append(correct_rate)
                correct_flist.append(correct_f)
                fause_flist.append(fause_f)
                accuracy.append(matomeaccu)

            np.savetxt(os.getcwd() + '/libs/opentest/loss.txt', losslist)  # 把loss存入文件中
            np.savetxt(os.getcwd() + '/libs/opentest/fause_rate.txt', fause_ratelist)
            np.savetxt(os.getcwd() + '/libs/opentest/correct_rate.txt', correct_ratelist)
            np.savetxt(os.getcwd() + '/libs/opentest/correct_f.txt', correct_flist)
            np.savetxt(os.getcwd() + '/libs/opentest/fause_f.txt', fause_flist)
            np.savetxt(os.getcwd() + '/libs/opentest/accuracy.txt', accuracy)

            Log.i("*** [OPENTESTDONE] ***")
            Log.i(" ")
            Log.i(" ")

if __name__ == "__main__":
    App.exec()