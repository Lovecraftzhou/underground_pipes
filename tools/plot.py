import numpy as np
from matplotlib import pyplot as plt
import math

fig = plt.figure()
ax = plt.axes(projection="3d")
x = y = np.arange(start=-4, stop=4, step=0.1)
X, Y = np.meshgrid(x, y)
Z = (1-3*(X**2)-3*(Y**2))
ax.plot_surface(X,Y,Z,alpha=0.9, cstride=1, rstride = 1, cmap='rainbow')
plt.show()
