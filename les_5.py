import random

size = 10
arr = [i for i in range(size)]
random.shuffle(arr)
print(arr)

def hoare_sort(array):
    if len(array) <= 1:
        return array
    pivot = random.choice(array)
    s_ar = []
    m_ar = []
    l_ar = []
    for el in array:
        if el < pivot:
            s_ar.append(el)
        elif el == pivot:
            m_ar.append(el)
        elif el > pivot:
            l_ar.append(el)
        else:
            raise Exception('Случилась неожиданность')
    return hoare_sort(s_ar) + m_ar + hoare_sort(l_ar)


def hoare_sort_no_mem(array, fst=0, lst=None):
    if lst is None or lst >= len(array):
        lst = len(array) - 1
    if fst >= lst:
        return
    # print(array)
    pivot = array[random.randint(fst, lst)]
    i, j = fst, lst
    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    hoare_sort_no_mem(array, fst, j)
    hoare_sort_no_mem(array, i, lst)


new_arr = hoare_sort(arr)
print(new_arr)
print('*'*50)

hoare_sort_no_mem(arr)
print('*'*5)
print(arr)
