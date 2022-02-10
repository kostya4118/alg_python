import sys, ctypes, struct

a = 5
b = 125.14
c = 'Hello, world!'

print(id(b))
print(sys.getsizeof(b))
print(ctypes.string_at(id(b), sys.getsizeof(b)))
print(struct.unpack('LLLLLd', ctypes.string_at(id(b), sys.getsizeof(b))))