import itertools

with open("rosalind_lgis.txt", "r") as file:
    data = file.readlines()
seq = list(map(int, data[1].split(" ")))
num = data[0]

n = 5
s_d = [5, 1, 4, 2, 3, 7]

def perm(number, sequence):
    pass