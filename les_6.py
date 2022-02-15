import random
from collections import namedtuple
from operator import attrgetter

size = 11
arr = [i for i in range(size)]
random.shuffle(arr)
print(arr)

def revers(array):
    for i in range(len(array) // 2):
        array[i], array[len(array) - i - 1] = array[len(array) - i - 1], array[i]


revers(arr)
print(arr)

arr.reverse()
print(arr)

arr.sort(reverse=True)
print(arr)
print('*' * 50)

t = tuple(random.randint(0, 100) for i in range(size))
print(t)
print(tuple(sorted(t, reverse=True)))
print('*' * 50)


Person = namedtuple('Person', 'name, age')
p1 = Person('Vasya', 25)
p2 = Person('Kolya', 30)
p3 = Person('Olya', 33)

peoples = [p1, p2, p3]
print(peoples)
print(sorted(peoples))

def by_age(person):
    return person.age

print(sorted(peoples, key=by_age))

print(sorted(peoples, key=attrgetter('age')))
