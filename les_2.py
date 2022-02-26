from collections import namedtuple

graph = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 0],
    [0, 1, 0, 0]
]

print(*graph, sep='\n')

print('*' * 50)

graph2 = [
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [0, 1, 0, 0],
    [0, 0, 0, 0]
]

print(*graph2, sep='\n')

print('*' * 50)

graph2[0][1:3] = [2, 3]
graph2[1][2] = 2
graph2[2][1] = 2

print(*graph2, sep='\n')

print('*' * 100)

graph3 = []
graph3.append([1, 2])
graph3.append([0, 2, 3])
graph3.append([0, 1])
graph3.append([1])

print(*graph3, sep='\n')
print('*' * 50)

graph3_2 = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1],
    3: [1]
}

print(graph3_2)
print(3 in graph3_2[1])

print('*' * 100)

Vertex = namedtuple('Vertex', ['vertex', 'edge'])
graph3_3 = []
graph3_3.append([Vertex(1, 2), Vertex(2, 3)])
graph3_3.append([Vertex(0, 2), Vertex(2, 2), Vertex(3, 1)])
graph3_3.append([Vertex(0, 3), Vertex(1, 2)])
graph3_3.append([Vertex(1, 1)])

print(*graph3_3, sep='\n')
for v in graph3_3[1]:
    if v.vertex == 3:
        print(True)


class Graph:
    def __init__(self, vertex, edge, spam):
        self.vertex = vertex
        self.edge = edge
        self.spam = spam



print('*' * 100)

graph4 = [(0, 1, 2), (0, 2, 3), (1, 2, 2), (1, 3, 1), (2, 1, 2)]

print(*graph4, sep='\n')
