
with open("DEG-data") as data:
    a = []
    data_graph = data.readlines()
    for line in data_graph[1:]:
        seq = list(map(int, line.split(" ")))
        a.append(seq)
    num_of_nodes = list(map(int, data_graph[0].split(" ")))[0]
    data.close()


def graph(data, n):
    b = {x: [] for x in range(1, int(n) + 1)}
    for key, value in b.items():
        for edge in data:
            if key in edge:
                x = edge.copy()
                x.remove(key)
                b[key].append(x[0])

    return b


def ddeg(dictionary):
    list_of_sums = []
    for key, value in dictionary.items():
        sum_of_edges = 0
        for node in value:
            sum_of_edges += len(dictionary[node])
        list_of_sums.append(sum_of_edges)
    print(" ".join(str(elem) for elem in list_of_sums))


dict_of_nodes = graph(a, num_of_nodes)
ddeg(dict_of_nodes)
