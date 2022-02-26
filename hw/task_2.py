g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]

def dijkarta(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    cost[start] = 0
    parent = [-1] * length
    min_cost = 0

    while min_cost < float('inf'):
        is_visited[start] = True
        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    path = {k: [] for k in range(length)}
    for i in range(length):
        if is_visited[i]:
            path[i].append(i)
            j = i
            while parent[j] != -1:
                path[i].append(parent[j])
                j = parent[j]
            path[i].reverse()

    return cost, path


s = int(input('От какой вершины идти: '))
cost, path = dijkarta(g, s)
print(cost)
for k, v in path.items():
    print(k, v)