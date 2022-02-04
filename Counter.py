from collections import Counter

a = Counter('abrakadabra')
b = Counter(cats = 4, dogs = 6)
c = Counter({'cats': 4, 'dogs': 6})
a['z'] = 0

print(a, b, c, sep='\n')
print(a['x'])
print(list(a.elements()))

print(a.most_common(2))

d = Counter(a=4, b=6, c=-2, d=0)
f = Counter(a=1, b=2, c=3, d=-3)
d.subtract(f)
print(d)
print('*' * 50)

d = Counter(a=4, b=6, c=-2, d=0)
print(d + f)
print(d - f)
print(d | f)
print(d & f)
print('*' * 50)
print(-d)
print(+d)
