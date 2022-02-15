import random

size = 10
arr = [i for i in range(size)]
random.shuffle(arr)
print(arr)

n = 1
while n < len(arr):
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    n += 1

    print(arr)