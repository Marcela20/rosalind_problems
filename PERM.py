from itertools import permutations


symbols = []
for i in range(1, 6 + 1):
    symbols.append(i)

perm = permutations(symbols)

counter = 0
a = ''
for i in list(perm):
    counter += 1
    for j in i:
        a += str(j)
        a += " "
    print(a)
    a = ''
print(counter)
