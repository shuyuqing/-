import os
import numpy as np

def _process():


    train_data = [];
    train_label = [];
    results = []
    batch_size = 3

    os.chdir(r'C:\Users\a7825\Desktop\工作空间\跑代码\实验用数据\F1\特征值')
    f = open('C.csv')
    a = np.loadtxt(f, delimiter=',', skiprows=0, ).astype(np.float32)
    print(a.shape)
    X = a[:, 1:None]
    #除去第一列，其他的都要
    print(X.shape)
    print(X)
    label = a[:, 0:1]
    N = X.shape[1]
    print(N)
    print('Xtrain reshape: {}'.format(X.shape))
    print('Ytrain reshape: {}'.format(label.shape))
    print('####################################')

    # train_data.append(X)
    # #append的话相当于在原来一维的基础上塞进了一个二维数组，变成了一个三维数组
    # train_label.append(label)
    #
    # train_data = np.array(train_data)
    # train_label = np.array(train_label)
    train_data = np.array(X)
    train_label = np.array(label)

    print('train_data')
    print(train_data)
    print(train_data.shape)
    print('train_label')
    print(train_label)
    print(train_label.shape)

    sample_size = len(train_data)
    print(sample_size)

    perm = np.random.permutation(sample_size)

    for i in range(0, sample_size, batch_size):
        #sample这个数字应该是很大的

        x_batch = train_data[perm[i:i + batch_size]]
        y_batch = train_label[perm[i:i + batch_size]]

        print('第%d波'%i)
        print(perm[i:i + batch_size])
        print(x_batch.shape)
        print(x_batch)
        print(y_batch.shape)
        print(y_batch)

if __name__ == "__main__":
    _process()
