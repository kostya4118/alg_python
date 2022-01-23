"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный
и максимальный элементы в сумму не включать.
"""

from random import randint

ar = [randint(0, 50) for _ in range(5)]

i_min, i_max = 0, 0
for i in range(1, len(ar)):
    if ar[i] < ar[i_min]:
        i_min = i
    if ar[i] > ar[i_max]:
        i_max = i

print(ar)
print(f'Минимальный элемент в массиве - {ar[i_min]}.\n'
      f'Максимальный элемент в массиве - {ar[i_max]}.')

summ = 0
if i_min + 1 < i_max:
    diap = range(i_min + 1, i_max)
    for i in diap:
        summ += ar[i]
    print(f'Сумма элементов, находящихся между ними - {summ}.')
elif i_max + 1 < i_min:
    diap = range(i_max + 1, i_min)
    for i in diap:
        summ += ar[i]
    print(f'Сумма элементов, находящихся между ними - {summ}.')
else:
    print('Между этими элементами ничего нет.')

