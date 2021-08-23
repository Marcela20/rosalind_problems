import numpy as np

with open("DEG-data") as data:
    a = []
    for line in data.readlines()[1:]:
        seq = list(map(int, line.split(" ")))
        a.append(seq)


def graph(data):
    b = []
    for i in np.array(data).flat:
        b.append(i)
    b = list(set(b))
    # b = dict.fromkeys(b)
    b = {x: [] for x in b}
    for key, value in b.items():
        for edge in data:
            if key in edge:
                b[key].append(edge)
    print(" ".join(str(elem) for elem in [len(y) for x, y in b.items()]))


graph(a)
