% matplotlib
inline
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve


def equations(p):
    x, y = p
    return (x ** 2 - 1 - y, np.exp(x) + x * (1 - y) - 1)


x = np.linspace(-2, 3, 201)
plt.figure(figsize=(6, 12))
plt.plot(x, (np.exp(x) + x - 1) / x)
plt.plot(x, x ** 2 - 1)
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-1, 5)
plt.grid(True)
plt.axis('equal')
plt.show()

x1, y1 = fsolve(equations, (2, 4))
x2, y2 = fsolve(equations, (-1, 1))

print(x1, y1)
print(x2, y2)
