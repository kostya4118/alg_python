"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно
разных значения.
"""

import random

ar = [random.uniform(-5, 5) for _ in range(7)]

print(ar)

max_neg_el = None

for j in range(len(ar)):
    if ar[j] < 0:
        max_neg_el, max_neg_i = ar[j], j
        for i in range(j + 1, len(ar)):
            if ar[i] < 0 and abs(ar[i]) < abs(max_neg_el):
                max_neg_el, max_neg_i = ar[i], i
        print(f'Максимальный отрицательный элемент - {max_neg_el}, он имеет индекс - {max_neg_i}.')
        break

if max_neg_el is None:
    print('Отрицательных чисел в массиве нет.')
