"""
На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
"""

n = int(input('Сколько друзей встретились: '))
g = [(i, j) for i in range(n) for j in range(n) if i != j]
print('Граф рукопожатий списком рёбер:', *g, sep="\n")

sets_list = []
for el in g:
    if set(el) not in sets_list:
        sets_list.append(set(el))
print('Количество рукопожатий:', len(sets_list))
