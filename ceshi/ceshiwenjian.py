import numpy as np
import os
from keras.layers import Reshape, Permute, Input
from keras.models import Model


path_baocun = r'C:\Users\a7825\Desktop\工作空间\语音数据\新建文件夹'
path_name = 'wenjian.npz'


# shuzu_1 = np.array([[1,2,3],[1,2,4]])
# shuzu_2 = np.array([[1,3,2],[2,3,1]])
# shuzu_3 = np.array([[2,1,3],[2,4,5]])
# shuzu_4 = np.array([[3,4,5],[2,7,8]])
# shuzu_5 = np.array([[[1,2],[2,5]],[[1,2],[2,5]]])

# shuzu_2 = np.concatenate((shuzu_1, shuzu_2), 0)

# print(shuzu_2)
# print(shuzu_5.shape)

# print(len(shuzu_5.shape))
# nb_epoch = 500
# tr_loss, val_loss, f1_overall_1sec_list, er_overall_1sec_list = [0] * nb_epoch, [0] * nb_epoch, [0] * nb_epoch, [0] * nb_epoch
# print(tr_loss)
# print(val_loss)



spec_x = [[[1,3],[4,7]],[[4,7],[8,6]],[[7,8],[1,2]]]
spec_x = np.array(spec_x)

spec_x_input = Input(shape=(spec_x.shape[-3], spec_x.shape[-2], spec_x.shape[-1]))

spec_x_output = Permute((2, 1, 3))(spec_x_input)
spec_x_output = Reshape((spec_x_output.shape[-2], -1))(spec_x_input)
_model = Model(inputs=spec_x_input,outputs=spec_x_output)

print(_model.summary())




