# import  socket
import numpy as np

def jiachuangzi(a):

    a = np.array(a,float)

    window = np.hamming(len(a))
    n=0
    for i in window:
        a[n] = a[n]*i
        n = n+1

    return a
