%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt


phi = np.linspace(1, 3, 2)
rho = np.linspace(1, 3, 2)
plt.polar(phi, rho)
plt.show()
