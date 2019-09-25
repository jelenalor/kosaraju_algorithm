""" Python 3.7
Author - Jelena Lor """

"""Load graph"""
with open(r"SCC.txt", "r") as f:
    data = f.readlines()

num_of_nodes = 875714 + 1
G = [set([]) for i in range(num_of_nodes)]
G_reverse = [set([]) for i in range(num_of_nodes)]

for line in data:
    item = line.split()
    G[int(item[0])].add(int(item[1]))
    G_reverse[int(item[1])].add(int(item[0]))

"""Load test cases"""
with open(r"test_case.txt", "r") as f:
    test = f.readlines()
num_of_nodes = 10
G_test = [set([]) for i in range(num_of_nodes)]
G_test_reverse = [set([]) for i in range(num_of_nodes)]

for line in test:
    item = line.split()
    if len(item) == 0:
        continue
    G_test[int(item[0])].add(int(item[1]))
    G_test_reverse[int(item[1])].add(int(item[0]))


def dfs_iter(graph, s):
    global colors
    global ordering
    global t
    stack = [s]
    while stack:
        vertex = stack.pop()
        if colors[vertex] != "F":
            stack.append(vertex)
            if colors[vertex] == "U":
                colors[vertex] = "D"

            all_adj_discover = True
            for w in list(graph[vertex]):
                if colors[w] == "U":
                    stack.append(w)
                    all_adj_discover = False
            if all_adj_discover:
                colors[vertex] = "F"
                t = t + 1
                ordering[vertex] = t


def dfs(graph, num_of_nodes):
    global colors
    global ordering
    global t
    # U - undiscovered, D - discovered, F - finished
    colors = ["U"] * num_of_nodes
    ordering = [0] * num_of_nodes
    t = 0
    for u in range(1, num_of_nodes)[::-1]:
        if colors[u] == "U":
            dfs_iter(graph, u)

    return ordering


ordering = dfs(G_test_reverse, 10)
print(ordering)
