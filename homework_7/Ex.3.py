import numpy as np


# изначальная линейная система не имеет решений, так как ранг ее расширенной матрицы не равен рангу матрицы основной
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[12], [2], [1]])
C = np.concatenate((A,B), axis=1)
print(f'Ранг основной и расширенной матрицы изначальной линейной системы: {np.linalg.matrix_rank(A, 0.0001), np.linalg.matrix_rank(C, 0.0001)}')

# при замене в правой части 12 на 3 получаем решение:
B1 = np.array([[3], [2], [1]])
C1 = np.concatenate((A,B1), axis=1)
print(f'Ранг основной и расширенной матрицы новой линейной системы: {np.linalg.matrix_rank(A, 0.0001), np.linalg.matrix_rank(C1, 0.0001)}')
np.linalg.lstsq(A, B1)
