import sys

sys.setrecursionlimit(50000)

def akk(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return akk(m - 1, 1)
    elif m > 0 and n > 0:
        return akk(m - 1, akk(m, n - 1))
    return f'Incorrect'

print(akk(3, 11))
