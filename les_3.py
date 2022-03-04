import hashlib

h_list = [None] * 26
def my_append(value):
    index = ord(value[0]) - ord('a')
    h_list[index] = value
    print(h_list)

# my_append('apricot')
# my_append('banana')
# my_append('apple')

def my_index(value):
    letter = 26
    index = 0
    size = 10000
    for i, char in enumerate(value):
        index += (ord(char) - ord('a') + 1) * letter ** i
    return index % size
#
# print(my_index('apricot'))
# print(my_index('banana'))
# print(my_index('apple'))

print(hashlib.sha1(b'Hello, World!').hexdigest())
print(hashlib.sha1(b'password' + b'Hello, World.').hexdigest())


s = hashlib.sha1(b'Hello, World!').hexdigest()
print(s.encode('utf-8'))
print(hashlib.sha1(b'password' + bytes(s.encode('utf-8'))).hexdigest())