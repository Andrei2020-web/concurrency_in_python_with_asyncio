'''
Вычисление средних в большой матрице
с помощью NumPy
'''
import numpy as np
import time

data_points = 1000000000
rows = 50
columns = int(data_points / rows)
# создает массив целочисленных элементов, затем мы реорганизуем массив
# в матрицу с 50 строками
matrix = np.arange(data_points).reshape(rows, columns)

start_time = time.time()
# вычислить средние по строкам
res = np.mean(matrix, axis=1)

end_time = time.time()
print(end_time - start_time)
