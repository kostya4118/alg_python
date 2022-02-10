li = []
li.append(1)
li.extend([2,3,4])
print(li)

li.insert(1, 5)
print(li)

last = li.pop()
print(li, last)

last = li.pop()
print(li, last)

li.remove(5)
print(li)


# allocated = 0
# for newsize in range(100):
#     if allocated < newsize:
#         new_allocated = (newsize >> 3) + (3 if newsize < 9 else 6)
#         allocated = newsize + new_allocated
#     print(allocated, newsize)