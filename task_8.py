"""
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять
сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести
полученную матрицу.
"""


def print_matrix(matrix):
    for line in matrix:
        for el in line:
            print(f'{el:>8}', end='')
        print()
    print()


matrix = []
line = None
for i in range(5):
    while True:
        try:
            s = input(f'Введите через пробел 3 элемента строки {i + 1}: ').split()
            if len(s) != 3:
                print("Некорректный ввод!")
                continue
            line = []
            for el in s:
                line.append(float(el))
            break
        except ValueError:
            print("Некорректный ввод!")
    summ = 0
    for el in line:
        summ += el
    line.append(summ)
    matrix.append(line)

print_matrix(matrix)
