"""Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""

def eratosfen(n):
    n += 1
    sieve = [el for el in range(n)]
    sieve[1] = 0

    for i in range(2, n):
        if sieve[i] != 0:
            j = i * 2
            while j < n:
                sieve[j] = 0
                j += i

    res = [el for el in sieve if el != 0]

    return res


def big_summ(li):
    digit = 0
    summ = 0
    for el in li:
        summ_el = 0
        s = str(el)
        for i in s:
            summ_el += int(i)
        if summ_el > summ:
            digit, summ = el, summ_el

    return {'digit': digit, 'summa': summ}


try:
    list_ = eratosfen(int(input('До какого числа определять простые числа: ')))
    for k, v in big_summ(list_).items():
        print(f'{k}: {v}')
except ValueError:
    print('Можно ввести только натуральное число!')
