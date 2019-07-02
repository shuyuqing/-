import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.contrib import rnn
import sklearn
from sklearn.cross_validation import KFold

# read the data,但是这样读进来的话，第一行数据就变成标签了，待会儿转化为numpy数组就少了第一行
df = pd.read_csv('data.csv')
#time_steps是RNN的一个属性值
time_steps = 10
# data preparation,len(df)是这堆数据的行数
label = np.zeros([len(df), 2])
#获得len(df)行，2列的全零矩阵
for i in range(len(df)):
    if float(df.iloc[i, [0]]) == 1.0:
        label[i, 0] = 1
    else:
        label[i, 1] = 1
#根据0/1标签来获得形如[[0. 1.][1. 0.][0. 1.][0. 1.]]这样的矩阵
feature = np.array(df.iloc[:, [i for i in range(1, len(df.columns))]])
#原数据的0、1标签去了，只保留特征值，但是少了第一行
def stack_data(arr, time_steps):
    x = []
    for i in range(len(arr) - time_steps):
        x.append(arr[i: i + time_steps])
    return np.array(x)

feature_val = stack_data(feature, time_steps)
label_val = label[time_steps:]

index_in_epoch = 0
def next_batch(perm_arr, train_x, train_y, batch_size):
#分批训练 每批数据的大小是batch_size
    global index_in_epoch
    start = index_in_epoch
    index_in_epoch += batch_size

    if index_in_epoch > len(train_x):
        np.random.shuffle(perm_arr)
        start = 0
        index_in_epoch = batch_size

    end = index_in_epoch
    return train_x[perm_arr[start:end]], train_y[perm_arr[start:end]]

# training parameters
learning_rate = 0.001
training_steps = 1000
batch_size = 50
display_step = 200

# model parameters
#timesteps = 10
num_input = len(df.columns) - 1 # data input
num_hidden = 128 # hidden neurons
n_layers = 3 # hidden layers
num_classes = 2 # total classes

# tf graph input
keep_prob = tf.placeholder(tf.float32)
#dropout部分
x = tf.placeholder("float", [None, time_steps, num_input])
y = tf.placeholder("float", [None, num_classes])
#先候住训练数据，再把训练数据传入函数，None的意思是无论给多少个训练数据都ok
#num_input是输入数据的次元,num_classes是输出数据的次元

# define weights and biases
#weight和biases的初始值设置为随机变量要比0要好得多
W = {
    'in': tf.Variable(tf.random_normal([num_input, num_hidden])),
    'out': tf.Variable(tf.random_normal([num_hidden, num_classes]))
}

b = {
    'in': tf.Variable(tf.random_normal([num_hidden])),
    'out': tf.Variable(tf.random_normal([num_classes]))
}


def RNN(x, weights, biases):

    # add input layer
    x_in = tf.reshape(x, [-1, num_input])
    x_in = tf.matmul(x_in, W['in']) + b['in']
    #matmul是矩阵的乘法
    x_in = tf.reshape(x_in, [-1, time_steps, num_hidden])

    # lstm cell
    layers = [rnn.BasicLSTMCell(num_hidden, forget_bias=1.0) for _ in range(n_layers)]

    # multilayer
    multi_layer = rnn.MultiRNNCell(layers)

    # dynamic lstm
    outputs, states = tf.nn.dynamic_rnn(multi_layer, x_in, dtype=tf.float32)

    #output layer
    logits=tf.matmul(states[-1][0], W['out']) + b['out']
	#把计算结果dropout掉一部分,
    logits = tf.nn.dropout(logits, keep_prob)
    return logits

logits = RNN(x, W, b)
prediction = tf.nn.softmax(logits)

# loss and optimizer
loss_op = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
    logits=logits, labels=y))
#求方差的平均值
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)
train_op = optimizer.minimize(loss_op)
#要使loss降到最小

# accuracy
correct_pred = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))
#比较输出的预测值和真实的预测值
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

# initializer
init = tf.global_variables_initializer()

def kfold_lstm(feature_val, label_val, num_folds = 4):
    kf = KFold(len(feature_val), n_folds = num_folds, shuffle = False)
    acc_list = []
    fold_index = 0

    for train_index, test_index in kf:
        fold_index += 1
        # train and test
        perm_arr = np.arange(len(train_index))
        np.random.shuffle(perm_arr)
        with tf.Session() as sess:

            # initialize
            sess.run(init)

            train_x = feature_val[train_index]
            train_y = label_val[train_index]
            test_x = feature_val[test_index]
            test_y = label_val[test_index]
            for step in range(1, training_steps+1):
                batch_x, batch_y = next_batch(perm_arr, train_x, train_y, batch_size)
                # train operation
                sess.run(train_op, feed_dict={x: batch_x, y: batch_y, keep_prob: 0.5})
#通过keep_prob来修改dropout的值
                if step % display_step == 0 or step == 1:
                    # Calculate batch loss and accuracy
                    loss, acc = sess.run([loss_op, accuracy], feed_dict={x: batch_x,
                                                                         y: batch_y, keep_prob: 1})
#不要丢弃loss跟acc，所以keep_prob设置为1
                    print("Step " + str(step) + ", Minibatch Loss= " + \
                          "{:.4f}".format(loss) + ", Training Accuracy= " + \
                          "{:.3f}".format(acc))

            print("Fold %d optimization finished!" % (fold_index))

            acc = sess.run(accuracy, feed_dict = {x: test_x, y: test_y, keep_prob: 1})
#run一下计算误差的部分
            acc_list.append(acc)
            print("Fold %d Testing Accuracy: %f" % (fold_index, acc))
    print('Test Accuracy: %f' % (np.mean(acc_list)))

kfold_lstm(feature_val, label_val, 4)
