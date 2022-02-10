import sys

print(sys.version, sys.platform, sep='\n')

a = 5
b = 125.14
c = 'Hello, world!'

print(sys.getsizeof(a))
print(sys.getsizeof(b))
print(sys.getsizeof(c))

d = [i for i in range(10)]
print(sys.getsizeof(d))



def show_size(x, level=0):
    print('\t' * level, f'type= {x.__class__}, size= {sys.getsizeof(x)}, object= {x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)

show_size(a)
show_size(b)
show_size(c)
show_size(d)
print('*' * 50)
show_size(tuple(d))
print('*' * 50)
show_size(set(d))
print('*' * 50)
di = {str(i): i for i in range(10)}
show_size(di)