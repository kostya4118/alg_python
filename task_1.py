"""Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции
 вводятся пользователем. После выполнения вычисления программа не завершается, а запрашивает новые данные для
 вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
 Если пользователь вводит неверный знак (не '0', '+', '-', '', '/'), программа должна сообщать об ошибке и снова
 запрашивать знак операции. Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел
 его в качестве делителя."""

stop = False
while stop == False:
    while True:
        znak = input('Введите знак операции (+, -, *, / или 0, чтобы выйти): ')
        if znak == '0':
            stop = True
            break
        elif znak in ('+', '-', '*', '/'):
            break
        else:
            print('Неверная операция')
    if stop == False:
        try:
            a = float(input('Введите первое число: '))
            b = float(input('Введите второе число: '))
            res = eval(f'{a}{znak}{b}')
            print(f'{a} {znak} {b} = {res}')
        except ZeroDivisionError:
            print('На 0 делить нельзя!')
        except ValueError:
            print('Можно использовать только числа!')
