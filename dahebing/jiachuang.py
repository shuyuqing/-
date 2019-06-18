# import  socket
import numpy as np

def jiachuangzi(a):

    a = np.array(a,float)

    window = np.hamming(len(a))
    n=0
    for i in window:
        print(i)
        a[n] = a[n]*i
        print(a[n])
        n = n+1

    return a
