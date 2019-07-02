import matplotlib.pyplot as plt
import numpy as np
from matplotlib import collections as matcoll

x = np.arange(1,13)
y = [15,14,15,18,21,25,27,26,24,20,18,16]

lines = []
for i in range(len(x)):
    pair=[(x[i],0), (x[i], y[i])]
    lines.append(pair)

linecoll = matcoll.LineCollection(lines)
fig, ax = plt.subplots()
ax.add_collection(linecoll)

plt.scatter(x,y)

plt.xticks(x)
plt.ylim(0,30)

plt.show() 
