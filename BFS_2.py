from _collections import defaultdict

with open("DEG-data") as data:
    lines = []
    data_graph = data.readlines()
    for line in data_graph[1:]:
        seq = list(map(int, line.split(" ")))
        lines.append(seq)
    num_of_nodes = list(map(int, data_graph[0].split(" ")))[0]


def graph(data, n):
    list_of_edges = [*range(1, int(n) + 1)]

    dict_graph = defaultdict(list)
    for e1, e2 in data:
        dict_graph[e1].append(e2)
    # print(dict_graph)
    return dict_graph


def bfs(dictionary, node, n):
    queue = []
    check_list = []
    check_list.append(node)
    queue.append(node)
    while queue != []:
        current = queue.pop(0)
        for nodes in dictionary[current]:
            if nodes not in check_list:
                queue.append(nodes)
                check_list.append(nodes)
    print(check_list)

bfs(graph(lines, num_of_nodes), 1, num_of_nodes)
