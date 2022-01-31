import numpy as np
import math


k, n = 0, 10000
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
e = np.random.randint(0, 2, n)
x = a + b + c + d + e
for i in range(0, n):
  if x[i] == 4:
    k += 1
cnk = math.factorial(5) / (math.factorial(4) * math.factorial(5 - 4))
pnk = cnk * (0.5 ** 4) * (0.5 ** (5 - 4))
print (f'Фактический результат: {k, n, k / n}')
print (f'Расчётный результат: {pnk}')
