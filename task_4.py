"""Определить, какое число в массиве встречается чаще всего."""

from random import randint

ar = [randint(-5, 5) for _ in range(77)]

print(ar)

nums = set(ar)

big_nums = []
big_count = 0

for el in nums:
    count = 0
    for n in ar:
        if n == el:
            count += 1
    if big_count < count:
        big_count = count

for el in nums:
    count = 0
    for n in ar:
        if n == el:
            count += 1
    if big_count == count:
        big_nums.append(el)

if len(big_nums) > 1:
    print(f'Числа {", ".join(map(str, big_nums))} в массиве встречаются чаще всего - по {big_count} раз.')
else:
    print(f'Число {big_nums[0]} в массиве встречается чаще всего - {big_count} раз.')
