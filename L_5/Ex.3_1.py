import numpy as np
import math


k, n = 0, 10000
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
x = a + b + c + d
cnk = math.factorial(4) / (math.factorial(2) * math.factorial(4 - 2))
pnk = cnk * (0.5 ** 2) * (0.5 ** (4 - 2))
for i in range(0, n):
  if x[i] == 2:
    k += 1
print (f'Фактический результат: {k, n, k / n}')
print (f'Расчётный результат: {pnk}')
