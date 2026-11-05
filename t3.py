import numpy as np

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print("Исходная матрица:")
for row in matrix:
    print(row)
print('Траспонированная матрица')
# Через numpy
trans_matrix = np.transpose(matrix)
#через zip
for row in zip(*matrix):
    print(list(row))