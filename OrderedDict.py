from collections import OrderedDict, defaultdict, deque

n = 3000
with open('big_log.txt', 'r', encoding='utf-8') as f:
    log = deque(f, n)
data = OrderedDict()
spam = defaultdict(int)

for el in log:
    ip = el[:-1]
    if not ip.startswith('192.168.'):
        spam[ip] += 1
        data[ip] = 1
# print(spam, data, sep='\n\n')

data.update(spam)
# print(data)

with open('my_log.txt', 'w', encoding='utf-8') as f:
    for k, v in data.items():
        f.write(f'{k} - {v}\n')

# a = {'cat': 5, 'mouse': 1, 'dog': 3}
# a_new = OrderedDict(sorted(a.items(), key=lambda x: x[0]))
# print(a_new)
#
# b = {'dog': 3, 'cat': 5, 'mouse': 1}
# b_new = OrderedDict(sorted(b.items(), key=lambda x: x[1]))
# print(b_new)
#
# print(a == b)
# print(a_new == b_new)
#
# b_new.move_to_end('dog')
# print(b_new)
# b_new.move_to_end('cat', last=False)
# print(b_new)
#
#
# b_new.popitem()
# print(b_new)
# a_new.popitem(last=False)
# print(a_new)
#
# a_new['cow'] = 7
# print(a_new)
# a_new['dog'] = 7
# print(a_new)
# print('*' * 50)
#
# c_new = OrderedDict(sorted(a.items(), key=lambda x: len(x[0])))
# print(c_new)
# for key in reversed(c_new):
#     print(key, c_new[key])