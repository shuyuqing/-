#!/usr/bin/env python
# -*- coding: utf-8 -*-

#用的chainer版本是1.24
#注意，关于入力数据，要先把array塞入list,然后再把list变成array
import sys,os,label
sys.path.append('/mnt/userdata/kokann/test')
sys.path.append('/root/.pyenv/versions/anaconda3-5.0.0/envs/py3/lib/python3.4/site-packages/chainer/links')
from chainer import cuda, optimizers, serializers,Variable
from chainer.optimizer import WeightDecay, GradientClipping
from model_cross import BLSTM #3norm, 4midlelayer, 5Thres
import config as cfg
from libs.base import App as AbstractApp, Logger as Log
import numpy as np
from sklearn.metrics import confusion_matrix

def train(
        n_epoch=10,  # 20
        batch_size=10,  # 20
        #n_epoch和batch_size在这里设置是没用的
        #但是记住，每次把它们调整成一样的
        gpu=-1,
        save=True
):
    hparams = {
        'batchsize': cfg.batchsize,
        'dropout_ratio': cfg.dropout,
        'adagrad_lr': cfg.adagrad_lr,  # 0.0005 < lr < 0.01
        'weight_decay': 0.0001,  # 0.0001
        'inputN':cfg.inputN,
        'output':cfg.outputN,
        'lr':cfg.lr,
        'lstmcenshu':cfg.lstmcenshu,
        'cudnn':cfg.cudnn,
        'embed_size':cfg.embed_size,
        'xunliandata':(str(cfg.gakusyu)).encode(encoding = 'utf-8'),#如果要保存字符串的话得重新编码
        'mse':cfg.mse,
        'cross':cfg.cross,
    }

    Log.v('')
    Log.v("initialize ...")
    Log.v('--------------------------------')
    Log.i('# Minibatch-size: %d' % cfg.batchsize)
    Log.i('# epoch: %d' % cfg.epoch)
    Log.i('# gpu: %d' % cfg.gpu)
    Log.i('# hyper-parameters: %s' % str(hparams))
    Log.v('--------------------------------')
    Log.v('')

    train_data = []
    train_label = []

    # Set Training data
    pathDir = os.listdir(cfg.gakusyu)
    # print(pathDir)
    cot = 0
    for allDir in pathDir:
        # print(allDir)
        allDir = os.path.join(cfg.gakusyu, allDir)

        f = open(allDir, 'r')
        print("我读到了文件%s"%allDir)
        a = np.loadtxt(f, delimiter=',', skiprows=0).astype(np.float32)
        Xtrain = a[:, 1:None]
        Labeltrain = a[:, 0:1]
        # skl.preprocessing.normalize(Xtrain, norm='l2')
        #这是用来干什么的暂时不知道
        # ds = X.shape[0]
        # print('Xtrain shape: {}'.format(Xtrain.shape))
        if cfg.cross == True:

            Labeltrain = label.label_2(Labeltrain)

            train_label.append(np.array(Labeltrain, np.int32))
            train_data.append(np.array(Xtrain, np.float32))

        if cfg.mse == True:

            Labeltrain = label.label_1(Labeltrain)

            train_label.append(np.array(Labeltrain, np.float32))
            train_data.append(np.array(Xtrain, np.float32))

#把形如[[0],[1]]的标签变成形如[[1,0],[0,1]]的标签
    train_data = np.array(train_data)
    train_label = np.array(train_label)

    # print("现在打印所有的标签")
    # print(train_label)
    # print(len(train_label))
    # print("现在打印所有的学习数据")
    # print(type(train_label))
    # print(train_data)

    sample_size = len(train_data)
    print("我们的学习数据一共有%d个"%sample_size)
    # Set up a neural network
    cls = BLSTM
    model = cls(
        f_dim = cfg.inputN,
        n_labels = cfg.outputN,  # (11*2) +1,
        dropout = hparams['dropout_ratio'],
        train = True,

    )

    if gpu >= 0:
        cuda.get_device_from_id(gpu).use()
        model.to_gpu()
        # cuda.get_device_from_id(gpu)
        # model.to_gpu()

    optimizer = optimizers.Adam(alpha=cfg.lr)
    optimizer.setup(model)
    # optimizer.add_hook(WeightDecay(hparams['weight_decay']))
    losslist = []
    fause_ratelist=[]
    correct_ratelist=[]
    correct_flist=[]
    fause_flist=[]


#从这里开始，训练和更新参数的代码都写在这里面了
    for epoch in range(n_epoch):
        print("第%d个epoch的训练开始训练" % (epoch+1))

        batch_count = 0
        loss = 0.0
        accuracy = 0.0

        perm = np.random.permutation(sample_size)

        y_batch_1 = []
        yucezhi_1 = []

        for i in range(0, sample_size, batch_size):#sample_size是语音数据的总个数，每一次循环就是一次训练，每一次训练使用batch_size个数据
            # print("第%d次正向传播,这次正向传播的batch_size是%d"%((i/batch_size)+1,batch_size))

            x_batch = train_data[perm[i:i + batch_size]]
            y_batch = train_label[perm[i:i + batch_size]]

            batch_count += 1
            # print("这次正向传播的学习数据一共有%d个"%len(x_batch))
            # print("下面是x_batch")
            # print(x_batch)
            # print("这次正向传播的学习数据的标签的个数有%d个"%len(y_batch))
            # print("下面是y_batch")
            # print(y_batch)
            # model.cleargrads()

            batch_loss,preds_1, yucezhi = model(x_batch, y_batch)  # 只要是往实例里面传递参数，就是调用了_call_函数
            # 把batch_size传进去，才方便计算loss
            # print(y_batch)
            # print(yucezhi)
            # os.system("pause")


            for a in y_batch:
                # print(type(a))
                # os.system("pause")
                y_batch_1.extend(a.tolist())

            for b in yucezhi:
                # print(type(b.data))
                # os.system("pause")
                yucezhi_1.extend((b.data).tolist())#加了tolist居然好使了



            print("下面打印的是这次正向传播的loss")
            print(batch_loss.data)

            loss += batch_loss.data
            # print("下面打印的是这次正向传播的准确率")
            # print(batch_accuracy)
            # accuracy += batch_accuracy
            # print("下面打印叠加之后的loss")
            # print(loss)
            print("下面打印batch_count")
            print(batch_count)

            # 这部分代码是胡欢的
            # optimizer.target.cleargrads()
            # loss.backward()
            # optimizer.update()

            # 这部分代码是后藤的
            # optimizer.target.zerograds()
            # loss.backward()
            # # loss.unchain_backward()#如果训练数据太长的话，比如说可以规定每过30个数据忘记一次参数，想要忘记参数的话就调用一次这个函数
            # optimizer.update()
            if model.train == True:
                optimizer.target.zerograds()
                batch_loss.backward()
                batch_loss.unchain_backward()
                optimizer.update()

        confuse = confusion_matrix(y_batch_1, yucezhi_1)  # 注意如果输出值跟真实值完全一致，且值都是0或者都是1，它只会输出一维的列表

        fause = confuse[1][1] / (confuse[1][0] + confuse[1][1])
        # fause_1 = confuse[1][1] / (confuse[0][1] + confuse[1][1])
        correct = confuse[0][0] / (confuse[0][0] + confuse[0][1])
        # correct_1 = confuse[0][0] / (confuse[0][0] + confuse[1][0])
        # c = confuse[0][0] + confuse[0][1]
        # f = confuse[1][0] + confuse[1][1]
        # all = confuse[0][0] + confuse[0][1] + confuse[1][0] + confuse[1][1]
        # correct_f = (2 * correct * correct_1) / (correct + correct_1)
        # fause_f = (2 * fause * fause_1) / (fause + fause_1)
        # correct_f = correct_f/batch_count
        # fause_f = fause_f/batch_count

        print("本次epoch训练完之后的总的loss跟batch_count是")
        print(loss)
        print(batch_count)

        Log.i("[%s] epoch %d - - #samples: %d, loss: %f, fause_rate: %f, correct_rate: %f"
              % ('training' if model.train else 'evaluation', epoch + 1, sample_size, loss / batch_count,fause,correct))
        Log.v('-')
        loss_1 = loss/batch_count
        losslist.append(loss_1 / batch_size)#这里计算出来的loss就是每个语音文件的loss
        fause_ratelist.append(fause)
        correct_ratelist.append(correct)
        print("现在把第%d个epoach的模型保存下来")
        name = str(epoch+1) + 'model'
        Log.i("saving the model to %s ..." %(epoch+1)+'model')
        serializers.save_npz(os.path.join(os.getcwd()+'/model/',name), model)
    np.savetxt(os.getcwd()+'/libs/train/loss.txt',losslist)#把loss存入文件中
    np.savetxt(os.getcwd() + '/libs/train/fause_rate.txt', fause_ratelist)
    np.savetxt(os.getcwd() + '/libs/train/correct_rate.txt', correct_ratelist)
    # if save is not None:
    #     save = cfg.modelname
    #     Log.i("saving the model to %s ..." % save)
    #     serializers.save_npz(save, model)