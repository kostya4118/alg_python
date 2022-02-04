"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого
предприятия.Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
предприятий, чья прибыль выше среднего и ниже среднего.
"""

from collections import namedtuple

while True:
    try:
        count = int(input('Введите количество предприятий: '))
        if count <= 0:
            raise ValueError
        else:
            break
    except ValueError:
        print('Должно быть целое число больше нуля!')
firms = {'all': [], 'good': [], 'bad': []}
profit_all = 0
for i in range(count):
    while True:
        name = input(f'Введите название предприятия {i+1}: ')
        if name == '':
            print('Вы не ввели название!')
        else:
            break
    while True:
        try:
            profits = list(map(float, input(f'Введите через пробел прибыль за каждый из четырёх '
                                            f'кварталов для предприятия {name}: ').split()))
            if len(profits) != 4:
                raise ValueError
            else:
                break
        except ValueError:
            print('Введены некорректные значения!')
    profit_year = sum(profits)
    New_Firm = namedtuple('New_Firm', 'name q1 q2 q3, q4, yr')
    firm = New_Firm(name, profits[0], profits[1], profits[2], profits[3], profit_year)
    profit_all += firm.yr
    firms['all'].append(firm)
profit_mid = profit_all / count
print(f'Средняя прибыль для всех предприятий: {profit_mid}')
for el in firms['all']:
    if profit_mid < el.yr:
        firms['good'].append(el.name)
    elif profit_mid > el.yr:
        firms['bad'].append(el.name)
print(f"Предприятия, чья прибыль выше среднего - {', '.join(firms['good'])}.\n"
      f"Предприятия, чья прибыль ниже среднего - {', '.join(firms['bad'])}.")
