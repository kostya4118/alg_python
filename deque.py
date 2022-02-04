from collections import deque

a = deque()
b = deque('abcdef')
c = deque([1, 2, 3, 4, 5])
print(a, b, c, sep='\n')

b = deque('abcdef', maxlen=4)
c = deque([1, 2, 3, 4, 5], maxlen=3)
print(a, b, c, sep='\n')
a.clear()
print('*' * 50)

d = deque([i for i in range(5)], maxlen=5)
d.append(5)
d.appendleft(6)
print(d)
d.extend([7, 8, 9])
d.extendleft([10, 11])
print(d)
print('*' * 50)

f = deque([i for i in range(5)], maxlen=7)
x = f.pop()
y = f.popleft()
print(x, y, f, sep='\n')
print('*' * 50)

g = deque([i for i in range(1, 7)], maxlen=7)
print(g.count(2))
print(g.index(4))
g.insert(2, 85)
print(g)

g.reverse()
print(g)

g.rotate(-2)
print(g)
g.rotate(1)
print(g)
print('*' * 50)

with open('big_log.txt', 'r', encoding='utf-8') as f:
    lasl_five = deque(f, maxlen=5)
for ip in lasl_five:
    print(ip[:-1])