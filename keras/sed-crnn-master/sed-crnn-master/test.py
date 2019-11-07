from utils import hunxiao
from utils import hunxiao_1
from sklearn.metrics import confusion_matrix
import numpy as np

zhen = [0,0,0,0,0,1,1,1,1,1]
yuce = [1,1,1,0,0,1,1,1,1,1]

zhen = np.array(zhen)
yuce = np.array(yuce)


juzhen = confusion_matrix(zhen,yuce)

print(juzhen)

correct_f,fause_f,correct_rate,fause_rate = hunxiao(juzhen)

fause_f_1,correct_f_1 = hunxiao_1(juzhen)

print(fause_f)
print(correct_f)
print(fause_f_1)
print(correct_f_1)