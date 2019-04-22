#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import sklearn as sk
from sklearn.cross_validation import KFold

def kfold_lstm(feature_val, label_val, num_folds = 4):
    kf = KFold(len(feature_val), n_folds = num_folds, shuffle = False)
    # print(len(feature_val))
    # print(feature_val.shape)
    # print(len(kf))4折，所以它的长度肯定是4啊，
    # print(label_val)
    acc_list = []
    fold_index = 0

    for train_index, test_index in kf:
        print("TRAIN:", train_index, "TEST:", test_index)

        fold_index += 1
        # train and test
        perm_arr = np.arange(len(train_index))
        #arrange(3)会产生list[0,1,2]
        np.random.shuffle(perm_arr)
        # print(perm_arr)
        #打乱perm_arr这个list的顺序
        with tf.Session() as sess:

            # initialize
            sess.run(init)
            # print(feature_val)
            train_x = feature_val[train_index]
            # print(feature_val.shape)
            # print(train_x)
            train_y = label_val[train_index]
            test_x = feature_val[test_index]
            test_y = label_val[test_index]
            # print(test_y)
            for step in range(1, training_steps+1):
                batch_x, batch_y = next_batch(perm_arr, train_x, train_y, batch_size)
                # train operation
                sess.run(train_op, feed_dict={x: batch_x, y: batch_y})
                #每一次计算loss，都是用一个batchsize的数据训练完之后再去计算的
                #这里的train_op是输出

                #这里是自己添加的代码
                #把一个step之后的预测值输出来
                # print(sess.run(prediction1,feed_dict={x: batch_x, y: batch_y}))
                # tensorflow中要想把某个值输出来看看的话必需要run,还要给其他的变量赋初值
                #这里是自己添加的代码
                if step % display_step == 0 or step == 1:
                    # Calculate batch loss and accuracy
                    loss, acc = sess.run([loss_op, accuracy], feed_dict={x: batch_x,
                                                                         y: batch_y})
                    # print("Step " + str(step) + ", Minibatch Loss= " + \
                    #       "{:.4f}".format(loss) + ", Training Accuracy= " + \
                    #       "{:.4f}".format(acc))
                    print("Step " + str(step) + ", Minibatch Loss= %f" %loss , ", Training Accuracy= %f" %acc)

            print("Fold %d optimization finished!" % (fold_index))

            acc = sess.run(accuracy, feed_dict = {x: test_x, y: test_y})
            #直接把一个fold结束之后的预测值输出来
            #prediction1和tu是tensor类型的数据，现在把它转化为arry类型prediction2和tu1
            #prediction2表示预测的结果，tu2表示真实的结果，把这两个arry输入confuse 矩阵，计算他们的混淆矩阵
            prediction2 = sess.run(prediction1, feed_dict = {x: test_x, y: test_y})
            tu1 = sess.run(tu, feed_dict = {x: test_x, y: test_y})

            print("预测结果是:",prediction2)
            print("真实的情况是:",tu1)

            print("这个fold的混淆矩阵是："'\n',confusion_matrix(tu1, prediction2))
            '''
            混淆矩阵的形状是
                        预测值
                        0   1
            真实值  0   a   b
                    1   c   d
            真实值是0，预测值也是0的情况是有a次
            真实值是0，但是预测值是1的情况有b次。。。。。。
            '''
            # run这个变量相当于是得到了这个数据
            #run一下计算误差的部分
            acc_list.append(acc)
            # print("Fold %d confusion matirx:" %fold_index,confuse)

            print("Fold %d Testing Accuracy: %f" % (fold_index, acc))
    print('Test Accuracy: %f' % (np.mean(acc_list)))
