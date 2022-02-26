"""
Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
"""

import random

def create_graph(n):
    percent = random.uniform(0.5, 1)
    graph = {}
    for i in range(n):
        graph[i] = set()
        while len(graph[i]) < random.randrange(1, int(percent * n)):
            edge = random.randrange(0, n)
            if edge != i:
                graph[i].add(edge)
    return graph

def dfs(graph, start):
    path = []
    parent = [None for _ in range(len(graph))]
    is_visited = [False for _ in range(len(graph))]

    def _dfs(vertex):
        is_visited[vertex] = True
        path.append(vertex)
        for item in graph[vertex]:
            if not is_visited[item]:
                parent[item] = vertex
                _dfs(item)
                path.append(vertex)
        else:
            path.append(-vertex)

    _dfs(start)
    return parent, path

g = create_graph(int(input('Введите количество вершин графа: ')))
for k, v in g.items():
    print(k,'->', v)
s = int(input('С какой вершины начать обход графа: '))
parent, path = dfs(g, s)
print(parent)
print(path)