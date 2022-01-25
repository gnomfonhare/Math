%matplotlib inline
import numpy as np
from pylab import *
from mpl_toolkits.mplot3d import Axes3D

fig = figure()
ax = Axes3D(fig)
X = np.arange(-5, 5, 0.5)
Y = np.arange(-5, 5, 0.5)
X, Y = np.meshgrid(X, Y)
Z = 5 * X + 2 * Y
ax.plot_wireframe(X, Y, Z)
ax.plot_wireframe(X, Y, Z - 10)
show()
