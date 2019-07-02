import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.contrib import rnn
import sklearn
from sklearn.cross_validation import KFold

# read the data
df = pd.read_csv('data.csv')

time_steps = 10
# data preparation
label = np.zeros([len(df), 2])
for i in range(len(df)):
    if float(df.iloc[i, [0]]) == 1.0:
        label[i, 0] = 1
    else:
        label[i, 1] = 1
feature = np.array(df.iloc[:, [i for i in range(1, len(df.columns))]])
def stack_data(arr, time_steps):
    x = []
    for i in range(len(arr) - time_steps):
        x.append(arr[i: i + time_steps])
    return np.array(x)

feature_val = stack_data(feature, time_steps)
label_val = label[time_steps:]

index_in_epoch = 0
def next_batch(perm_arr, train_x, train_y, batch_size):
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
#training_steps只是进行优化的次数
#可以说是  梯度下降的次数吧

batch_size = 50
display_step = 200

# model parameters
#timesteps = 10
num_input = len(df.columns) - 1 # data input
num_hidden = 128 # hidden neurons
n_layers = 3 # hidden layers
num_classes = 2 # total classes

# tf graph input
x = tf.placeholder("float", [None, time_steps, num_input])
y = tf.placeholder("float", [None, num_classes])

# define weights and biases
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
    x_in = tf.reshape(x_in, [-1, time_steps, num_hidden])

    # lstm cell
    layers = [rnn.BasicLSTMCell(num_hidden, forget_bias=1.0) for _ in range(n_layers)]

    # multilayer
    multi_layer = rnn.MultiRNNCell(layers)

    # dynamic lstm
    outputs, states = tf.nn.dynamic_rnn(multi_layer, x_in, dtype=tf.float32)

    #output layer
    return tf.matmul(states[-1][0], W['out']) + b['out']

logits = RNN(x, W, b)
prediction = tf.nn.softmax(logits)

# loss and optimizer
loss_op = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
    logits=logits, labels=y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)
train_op = optimizer.minimize(loss_op)

# accuracy
correct_pred = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

# initializer
init = tf.global_variables_initializer()

#num_folds是默认参数，如果调用函数的时候不给它赋值，那么它就默认为4
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
                sess.run(train_op, feed_dict={x: batch_x, y: batch_y})
                if step % display_step == 0 or step == 1:
                    # Calculate batch loss and accuracy
                    loss, acc = sess.run([loss_op, accuracy], feed_dict={x: batch_x,
                                                                         y: batch_y})
                    print("Step " + str(step) + ", Minibatch Loss= " + \
                          "{:.4f}".format(loss) + ", Training Accuracy= " + \
                          "{:.3f}".format(acc))

            print("Fold %d optimization finished!" % (fold_index))

            acc = sess.run(accuracy, feed_dict = {x: test_x, y: test_y})
            acc_list.append(acc)
            print("Fold %d Testing Accuracy: %f" % (fold_index, acc))
    print('Test Accuracy: %f' % (np.mean(acc_list)))

kfold_lstm(feature_val, label_val, 4)
#如果要改成5折的话，把上面的4改成5就行了
