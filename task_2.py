"""
Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел
из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления, задача решается в
несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит. Поэтому использование встроенных
функций для перевода из одной системы счисления в другую в данной задаче под запретом.
"""

from collections import deque

toten = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
         '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
tohex = {}
for k, v in toten.items():
    tohex[v] = k


def summ(first, second):
    a = deque(first, maxlen=len(first))
    b = deque(second, maxlen=len(second))
    s = deque()
    spam = 0
    for i in range(a.maxlen if a.maxlen >= b.maxlen else b.maxlen):
        x = (toten[a[-1]] if len(first) > 0 else 0) + toten[b[-1]] + spam
        spam = x // 16
        x %= 16
        s.appendleft(tohex[x])
        a.appendleft('0')
        b.appendleft('0')
    if spam != 0:
        s.appendleft(tohex[spam])
    return s


def mult(first, second):
    a_fix = deque(first, maxlen=len(first))
    b = deque(second, maxlen=len(second))
    s = deque()

    for i in range(b.maxlen):
        eggs = deque()
        a = a_fix.copy()
        spam = 0
        dig = toten[b[-1]]
        for j in range(a.maxlen):
            x = toten[a[-1]] * dig + spam
            spam = x // 16
            x %= 16
            eggs.appendleft(tohex[x])
            a.appendleft('0')
        if spam != 0:
            eggs.appendleft(tohex[spam])
        eggs.extend(['0' for _ in range(i)])

        s = summ(s, eggs)
        b.appendleft('0')

    return s


while True:
    a = list(input('Введите первое число: ').upper())
    b = list(input('Введите второе число: ').upper())
    if a == [] or b == []:
        print('Поля должны быть заполнены!')
        continue
    for _ in a + b:
        if _ not in toten.keys():
            print('Можно вводить числа только в шестнадцатеричном формате!')
            break
    else:
        break

print(f'1-е число в виде массива: {a}\n'
      f'2-е число в виде массива: {b}\n'
      f'Сумма:                    {list(summ(a, b))}\n'
      f'Произведение:             {list(mult(a, b))}')
