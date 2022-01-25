%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace (-3 * np.pi, 3 * np.pi, 201)
k1 = 2
k2 = 3
k3 = 4
a1 = 1
a2 = 2
a3 = 3
b1 = 1
b2 = 2
b3 = 3
plt.plot(x, k1 * np.sin(x + a1) + b1)
plt.plot(x, k2 * np.sin(x + a2) + b2)
plt.plot(x, k3 * np.sin(x + a3) + b3)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show
