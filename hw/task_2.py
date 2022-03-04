"""
Закодируйте любую строку по алгоритму Хаффмана.
"""

import heapq
from collections import Counter, namedtuple

class Node(namedtuple('Node', ['left', 'right'])):
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')

class Leaf(namedtuple('Leaf', ['cher'])):
    def walk(self, code, acc):
        code[self.cher] = acc or '0'

def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, '')
    return code

def main(s):
    code = huffman_encode(s)
    encoded = ''.join(code[ch] for ch in s)
    print(encoded)


main(input('Введите строку: '))


# /usr/local/bin/python3.9 /Users/konstantin/PycharmProjects/alg_python/task_2.py
# Введите строку: Списывать нехорошо, но иногда приходится))
# 010101100111011111001011011001111100000110111101001011100001101001010101111101100001110100110111101101100110110001001111111111011001001011010001101001111010000111101100001000100
