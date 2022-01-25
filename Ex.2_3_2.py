%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt


phi = np.linspace (0, 10, 100)
plt.polar(phi, [10] * len(phi))
plt.show()
