from collections import defaultdict

a = defaultdict()
print(a)
print('*' * 50)

s ='egecsjyhgrdgkhtrbeqwj'
b = defaultdict(int)
for el in s:
    b[el] += 1
print(b)
print('*' * 50)

list_1 = [('cat', 1), ('dog', 5), ('cat', 2), ('mouse', 1), ('dog', 1), ('cat', 2)]
c = defaultdict(list)
for k, v in list_1:
    c[k].append(v)
print(c)
print('*' * 50)

list_2 = [('cat', 1), ('dog', 5), ('cat', 2), ('cat', 1), ('mouse', 1), ('dog', 1), ('dog', 5)]
d = defaultdict(set)
for k, v in list_2:
    d[k].add(v)
print(d)
print('*' * 50)

f = defaultdict(lambda: 'unknown')
f.update(rex='dog', tomas='cat')
print(f)
print(f['rex'])
print(f['jerry'])