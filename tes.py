import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
plt.close("all")

blues = plt.colormaps.get_cmap('Blues', 10)

fig, ax = plt.subplots()

l1 = np.array([1,2,3,4,5,6,7,8,9,10])
j=0
xaxis = np.linspace(0.5,1, 1000)
for i in range(0,10):
    l0 = l1*i
    print(l0)
    ax.plot(l1, l0,color = blues(xaxis[j]),label='plot')
    j+=1
    ax.legend()

plt.show()