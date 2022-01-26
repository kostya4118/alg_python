from random import randint

def bin_search(array, value):
    left = 0
    right = len(array) - 1
    pos = len(array) // 2

    while left <= right and array[pos] != value:
        if array[pos] > value:
            right = pos - 1
        else:
            left = pos + 1
        pos = (right + left) // 2

    if left > right:
        return f'Такого элемента в списке нет.'
    else:
        return f'Элемент {value} нахнаходятся на {pos + 1}-м месте.'

li = [randint(0, 1000) for i in range(50)]
li.sort()
print(li)
x = int(input('Какой элемент будем искать?: '))
print(bin_search(li, x))

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


def sum_col_row(matrix):
    sum_col = [0] * len(matrix[0])
    for line in matrix:
        sum_line = 0
        for i, el in enumerate(line):
            sum_line += el
            sum_col[i] += el
            print(f'{el:>5}', end='')
        print(f'   |  {sum_line}')
    print(f'-' * ((len(matrix[0])+2) * 5))
    for el in sum_col:
        print(f'{el:>5}', end='')
    print()


def invert_diag(matrix):
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            if i == j:
                matrix[i][j], matrix[i][size - 1 - j] = matrix[i][size - 1 - j], matrix[i][j]
    return matrix


matrix1 = get_matrix(0, 100, 5, 4)
sum_col_row(matrix1)
# print_matrix(matrix1)
# print_matrix(invert_diag(matrix1))