"""
2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте
его улучшить/оптимизировать под задачу.
Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
"""

def eratosfen(num):
    n = 1
    li = [2]
    while len(li) < num:
        n *= 10
        sieve = [el for el in range(n)]
        sieve[1] = 0
        for i in range(2, n):
            if sieve[i] != 0:
                j = i * 2
                while j < n:
                    sieve[j] = 0
                    j += i
        li = [el for el in sieve if el != 0]

    return li[num-1]


def classic_prime(num):
    li = [2]
    while len(li) < num:
        last = li[-1]
        while True:
            last += 1
            for el in li:
                if last % el == 0:
                    break
            else:
                li.append(last)
                break

    return li[-1]


print(eratosfen(4000))
print(classic_prime(4000))
