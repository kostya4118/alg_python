import random

size = 10
arr = [i for i in range(size)]
random.shuffle(arr)
print(arr)

def selection_sort(array):
    for i in range(len(array)):
        idx_min = i
        for j in range(i + 1, len(array)):
            if array[j] < array[idx_min]:
                idx_min = j
        array[i], array[idx_min] = array[idx_min], array[i]


selection_sort(arr)
print(arr)