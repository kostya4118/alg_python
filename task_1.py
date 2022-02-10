'''Подсчитать, сколько было выделено памяти под переменные'''

import sys

print(sys.version, sys.platform, sep='\n')

# 3.9.4 (v3.9.4:1f2e3088f3, Apr  4 2021, 12:32:44)
# [Clang 6.0 (clang-600.0.57)]
# darwin


# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне
# от 2 до 9. Примечание: 8 разных ответов.

class ShowSize():

    def __init__(self):
        self._sum_mem = 0

    def _add(self, obj):
        spam = sys.getsizeof(obj)
        self._sum_mem += spam

        if hasattr(obj, '__iter__'):
            if hasattr(obj, 'items'):
                for el in obj.items():
                    self._add(el)
            elif not isinstance(obj, str):
                for el in obj:
                    self._add(el)

    def extend(self, *args):
        for i in args:
            self._add(i)

    def print_sum(self):
        print(f'Переменные функции заняли {self._sum_mem} байт памяти')


# АЛГОРИТМ 1

list_big = [2, 99]
list_lit = [2, 9]

li = [0] * (list_lit[1] + 1)
for i in range(list_big[0], list_big[1] + 1):
    for n in range(list_lit[0], list_lit[1] + 1):
        if i % n == 0:
            li[n] += 1
s = ''
for i, el in enumerate(li[list_lit[0]:], list_lit[0]):
    s += f'{el} чисел из диапазона кратны {i}.\n'
# print(s)

summary1 = ShowSize()
summary1.extend(list_big, list_lit, li, s)
summary1.print_sum()

# Переменные функции заняли 1250 байт памяти


# АЛГОРИТМ 2

dicT = {}
for i in range(list_big[0], list_big[1] + 1):
    for n in range(list_lit[0], list_lit[1] + 1):
        if i % n == 0:
            if n in dicT:
                dicT[n] += 1
            else:
                dicT[n] = 1
s = ''
for k, v in dicT.items():
    s += f'{v} чисел из диапазона кратны {k}.\n'
# print(s)

summary2 = ShowSize()
summary2.extend(list_big, list_lit, dicT, s)
summary2.print_sum()

# Переменные функции заняли 2098 байт памяти


# АЛГОРИТМ 3

li = [n for n in range(list_big[0], list_big[1] + 1)]
s = ''
for i in range(list_lit[0], list_lit[1] + 1):
    count = 0
    for n in li:
        if n % i == 0:
            count += 1
    s += f'{count} чисел из диапазона кратны {i}.\n'
# print(s)

summary3 = ShowSize()
summary3.extend(list_big, list_lit, li, count, s)
summary3.print_sum()

# Переменные функции заняли 4534 байт памяти

"""
Вывод: первый алгоритм наиболее экономичный по пямяти, поскольку использует значительно меньший список, нежели алгоритм
№3, и не использует словарь, как алгоритм №2.
"""
