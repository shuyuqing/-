import numpy as np
np.random.seed(1337)  # for reproducibility
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
from keras.optimizers import Adam
from keras.regularizers import L1L2

# create some data
X = np.linspace(-1, 1, 200)
np.random.shuffle(X)    # randomize the data
Y = 0.5 * X + 2 + np.random.normal(0, 0.05, (200, ))
# plot data
plt.scatter(X, Y)
plt.show()

X_train, Y_train = X[:160], Y[:160]     # first 160 data points
X_test, Y_test = X[160:], Y[160:]       # last 40 data points

# build a neural network from the 1st layer to the last layer
model = Sequential()

model.add(Dense(units=1, input_dim=1))

# choose loss function and optimizing method
adam = Adam(lr = 0.01)#说明还是可以更改学习率的
model.compile(loss='mse', optimizer=adam)

# training
print('Training -----------')
for step in range(301):
    cost = model.train_on_batch(X_train, Y_train)#训练的时候有两种方式，一种是train_on_batch,另外一种是fit函数
    if step % 100 == 0:
        print('train cost: ', cost)

# test
print('\nTesting ------------')
cost = model.evaluate(X_test, Y_test, batch_size=40)
print('test cost:', cost)
model.save('model.h5')#保存训练好的模型，先要安装的东西：pip install h5py

W, b = model.layers[0].get_weights()
print('Weights=', W, '\nbiases=', b)

# plotting the prediction
Y_pred = model.predict(X_test)
plt.scatter(X_test, Y_test)
plt.plot(X_test, Y_pred)
plt.show()