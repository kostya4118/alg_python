from collections import ChainMap
import argparse

default = {'ip': 'localhost', 'port': 7777}

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--ip')
parser.add_argument('-p', '--port')

args = parser.parse_args()
new_dict = {k: v for k, v in vars(args).items() if v}

settinds = ChainMap(new_dict, default)
print(settinds['ip'])
print(settinds['port'])


# d1 = {'a': 1, 'b': 2, 'c': 3}
# d2 = {'a': 10, 'b': 20, 'd': 40}
# d = ChainMap(d1, d2)
# print(d)
#
# d1['a'] = 100
# print(d)
#
# print(d['b'])
# print(d['d'])
# print('*' * 50)
#
# x = d.new_child({'a': 111, 'b': 112, 'c': 113})
# print(x)
#
# print(x.maps[1])
#
# print(x.parents)
# print('*' * 50)
#
# y = d.new_child()
# print(y)
# print(y['a'])
# y['a'] = 76
# print(y)
# print(y['a'])
#
# print(list(y))
# print(list(y.values()))
