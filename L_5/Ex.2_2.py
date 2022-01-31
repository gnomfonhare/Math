%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt


x0 = np.sum(np.random.rand(100))
x1 = np.sum(np.random.rand(100))
x2 = np.sum(np.random.rand(100))
x3 = np.sum(np.random.rand(100))
x4 = np.sum(np.random.rand(100))
x5 = np.sum(np.random.rand(100))
x6 = np.sum(np.random.rand(100))
x7 = np.sum(np.random.rand(100))
x8 = np.sum(np.random.rand(100))
x9 = np.sum(np.random.rand(100))
xs = (x0, x1, x2, x3, x4, x5, x6, x7, x8, x9)
print(xs)
num_bins = 5
n, bins, patches = plt.hist(xs, num_bins)
plt.xlabel('x')
plt.ylabel('Probability')
plt.title('Histogram')
