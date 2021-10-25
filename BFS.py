from _collections import defaultdict

with open("DEG-data") as data:
    lines = []
    data_graph = data.readlines()
    for line in data_graph[1:]:
        seq = list(map(int, line.split(" ")))
        lines.append(seq)
    num_of_nodes = list(map(int, data_graph[0].split(" ")))[0]


def graph(data, n):
    dict_graph = {x: [] for x in range(1, int(n) + 1)}
    for key, value in dict_graph.items():
        for edge in data:
            if key == edge[0]:
                dict_graph[key].append(edge[1])

    return dict_graph
def bfs(dictionary, node):
    list_of_floors = [[node]]
    distances = []
    check_list = [node]
    while list_of_floors[-1] != []:
        next_floor = []
        for i in list_of_floors[-1]:
            for y in dictionary[i]:
                if y not in next_floor and y not in check_list:
                    next_floor.append(y)
                    check_list.append(y)
        list_of_floors.append(next_floor)

    for i in dictionary:
        print(i)
        check_list = []
        for floor in list_of_floors[:-1]:
            if i in floor:
                distances.append(list_of_floors.index(floor))
                check_list.append(1)
        if check_list == []:
            distances.append(-1)
    # print(" ".join(str(elem) for elem in distances))
    print(list_of_floors)



bfs(graph(lines, num_of_nodes), 1)
