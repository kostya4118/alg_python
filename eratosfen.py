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

if __name__ == '__main__':
    print(eratosfen(997))
