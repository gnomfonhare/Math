%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace (0, 10, 101)
k_1 = 1
k_2 = 3
plt.plot(x, np.cos(k_1 * x))
plt.plot(x, np.cos(k_2 * x))
print(x)
