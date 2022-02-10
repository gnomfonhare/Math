import numpy as np
import scipy.linalg


A = np.array([[1, 2, 3], [2, 16, 21], [4, 28, 73]])
P, L, U = scipy.linalg.lu(A)
print(P)
print(L)
print(U)
print(np.dot(np.linalg.inv(P), A) - np.dot(L, U))

# эта часть задания есть в видео, но отсутвует в опизании практического задания
B = np.array([1, 2, 3])
np.linalg.solve(A, B)
