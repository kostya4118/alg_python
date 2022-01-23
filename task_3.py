"""В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""

from random import randint

ar = [randint(-50, 50) for _ in range(7)]

print(ar)

el_min, i_min, el_max, i_max = ar[0], 0, ar[0], 0

for i in range(1, len(ar)):
    if ar[i] > el_max:
        el_max, i_max = ar[i], i
    elif ar[i] < el_min:
        el_min, i_min = ar[i], i

ar[i_min], ar[i_max] = ar[i_max], ar[i_min]

print(ar)
