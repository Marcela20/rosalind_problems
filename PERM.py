from itertools import permutations

wyrazy = []
for i in range(1, 6 + 1):
    wyrazy.append(i)

perm = permutations(wyrazy)

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
