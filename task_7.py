"""
В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
(оба минимальны), так и различаться.
"""

from random import randint

ar = [randint(0, 50) for _ in range(10)]

min_1, min_2 = ar[0], ar[1]
for i in range(2, len(ar)):
    if ar[i] <= min_1 or ar[i] <= min_2:
        if min_1 <= min_2:
            min_2 = ar[i]
        else:
            min_1 = ar[i]

print(ar)
print(f'Два наименьших элемента массива - {min_1}, {min_2}.')
