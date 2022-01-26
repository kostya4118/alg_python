"""
Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать,
b. написать 3 варианта кода (один у вас уже есть),
c. проанализировать 3 варианта и выбрать оптимальный,
d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
e. написать общий вывод: какой из трёх вариантов лучше и почему.
"""


# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне
# от 2 до 9. Примечание: 8 разных ответов.

import cProfile

def multiplicity(list_big, list_lit):
    list = [n for n in range(list_big[0], list_big[1] + 1)]
    s = ''
    for i in range(list_lit[0], list_lit[1] + 1):
        count = 0
        for n in list:
            if n % i == 0:
                count += 1
        s += f'{count} чисел из диапазона кратны {i}.\n'
    return s

def multiplicity_dict(list_big, list_lit):
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
    return s

def multiplicity_list(list_big, list_lit):
    li = [0] * (list_lit[1] + 1)
    for i in range(list_big[0], list_big[1] + 1):
        for n in range(list_lit[0], list_lit[1] + 1):
            if i % n == 0:
                li[n] += 1
    s = ''
    for i, el in enumerate(li[list_lit[0]:], list_lit[0]):
        s += f'{el} чисел из диапазона кратны {i}.\n'
    return s


# multiplicity
# "task_1.multiplicity([2, 99], [2, 9])"
# 100 loops, best of 5: 46.5 usec per loop
# "task_1.multiplicity([2, 999], [2, 9])"
# 100 loops, best of 5: 435 usec per loop
# "task_1.multiplicity([2, 999], [2, 99])"
# 100 loops, best of 5: 4.3 msec per loop
# "task_1.multiplicity([2, 9999], [2, 99])"
# 100 loops, best of 5: 42.9 msec per loop

#multiplicity_dict
# "task_1.multiplicity_dict([2, 99], [2, 9])"
# 100 loops, best of 5: 75.3 usec per loop
# "task_1.multiplicity_dict([2, 999], [2, 9])"
# 100 loops, best of 5: 798 usec per loop
# "task_1.multiplicity_dict([2, 999], [2, 99])"
# 100 loops, best of 5: 5.03 msec per loop
# "task_1.multiplicity_dict([2, 9999], [2, 99])"
# 100 loops, best of 5: 49 msec per loop

#multiplicity_list
# "task_1.multiplicity_list([2, 99], [2, 9])"
# 100 loops, best of 5: 76.6 usec per loop
# "task_1.multiplicity_list([2, 999], [2, 9])"
# 100 loops, best of 5: 750 usec per loop
# "task_1.multiplicity_list([2, 999], [2, 99])"
# 100 loops, best of 5: 4.92 msec per loop
# "task_1.multiplicity_list([2, 9999], [2, 99])"
# 100 loops, best of 5: 47.8 msec per loop


# cProfile.run('multiplicity([2, 99], [2, 9])')
# 5 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 task_1.py:17(multiplicity)
# cProfile.run('multiplicity([2, 999], [2, 9])')
# 5 function calls in 0.001 seconds
# 1    0.000    0.000    0.001    0.001 task_1.py:17(multiplicity)
# cProfile.run('multiplicity([2, 999], [2, 99])')
# 5 function calls in 0.006 seconds
# 1    0.006    0.006    0.006    0.006 task_1.py:17(multiplicity)
# cProfile.run('multiplicity([2, 9999], [2, 99])')
# 5 function calls in 0.051 seconds
# 1    0.050    0.050    0.050    0.050 task_1.py:17(multiplicity)

# cProfile.run('multiplicity_dict([2, 99], [2, 9])')
# 5 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 task_1.py:28(multiplicity_dict)
# cProfile.run('multiplicity_dict([2, 999], [2, 9])')
# 5 function calls in 0.002 seconds
# 1    0.001    0.001    0.001    0.001 task_1.py:28(multiplicity_dict)
# cProfile.run('multiplicity_dict([2, 999], [2, 99])')
# 5 function calls in 0.007 seconds
# 1    0.007    0.007    0.007    0.007 task_1.py:28(multiplicity_dict)
# cProfile.run('multiplicity_dict([2, 9999], [2, 99])')
# 5 function calls in 0.054 seconds
# 1    0.054    0.054    0.054    0.054 task_1.py:28(multiplicity_dict)

# cProfile.run('multiplicity_list([2, 99], [2, 9])')
# 4 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 task_1.py:42(multiplicity_list)
# cProfile.run('multiplicity_list([2, 999], [2, 9])')
# 4 function calls in 0.001 seconds
# 1    0.001    0.001    0.001    0.001 task_1.py:42(multiplicity_list)
# cProfile.run('multiplicity_list([2, 999], [2, 99])')
# 4 function calls in 0.007 seconds
# 1    0.006    0.006    0.006    0.006 task_1.py:42(multiplicity_list)
# cProfile.run('multiplicity_list([2, 9999], [2, 99])')
# 4 function calls in 0.052 seconds
# 1    0.052    0.052    0.052    0.052 task_1.py:42(multiplicity_list)

"""
Данные алгоритмы имеют приблизительно одинаковую сложность. Однако, первый работает несколько быстрее, 
поскольку сразу формирует строку, без использования промежуточного словаря или списка.
"""