"""Найти максимальный элемент среди минимальных элементов столбцов матрицы."""

from random import randint

def get_matrix(min, max, row, col=None):
    if col == None:
        col = row
    ar = [[randint(min, max) for _ in range(col)] for _ in range(row)]
    return ar

def print_matrix(matrix):
    for line in matrix:
        for el in line:
            print(f'{el:>4}', end='')
        print()
    print()


matrix1 = get_matrix(0, 100, 4, 5)

max_min_el = None
for i in range(len(matrix1[0])):
    min_el = matrix1[0][i]
    for j in range(len(matrix1)):
        if matrix1[j][i] < min_el:
            min_el = matrix1[j][i]
    if max_min_el is None or max_min_el < min_el:
        max_min_el = min_el

print_matrix(matrix1)
print(max_min_el)