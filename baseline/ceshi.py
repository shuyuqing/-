import numpy as np
import os

i = [[1,1],[1,0],[0,1]]

i = np.array(i)
print(i.shape)

i = np.delete(i, [0,2], 0)

print(i)