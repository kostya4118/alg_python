import random

size = 1000
arr = [i for i in range(size)]
random.shuffle(arr)
print(arr)

def shell_sort(array):
    assert len(array) < 4000, "Массив слишком большой для этой сортировки!"

    def new_increment(array):
        inc = [1, 4, 10, 23, 57, 132, 301, 701, 1750]
        while len(array) >= inc[-1]:
            inc.pop()
        while len(inc) > 0:
            yield inc.pop()
    # count = 0
    for increment in new_increment(array):
        for i in range(increment, len(array)):
            for j in range(i, increment, -increment):
                if array[j - increment] <= array[j]:
                    break
                array[j], array[j - increment] = array[j - increment], array[j]
    #             count += 1
    # print(count)


shell_sort(arr)
print(arr)
