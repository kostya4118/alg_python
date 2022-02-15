"""
 Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой
 называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в
 другой — не больше медианы.
Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод
сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
"""


import random
import numpy


def get_median(array):
    array = array.copy()
    while len(array) > 1:
        minim = maxim = array[0]
        for el in array:
            if el < minim:
                minim = el
            if el > maxim:
                maxim = el
        array.remove(minim)
        array.remove(maxim)
    return array[0]


m = random.randint(1, 100)
arr = [random.randint(-100, 100) for i in range(2 * m + 1)]
print(f'Исходный массив:\n{arr}')
print(f'Медиана, найденная чемез функцию: {get_median(arr)}')
print(f'Медиана, найденная чемез numpy: {numpy.median(arr)}')
