from Bio import SeqIO

sequences = open("rosalind_cons.txt")
seq_list = []

for record in SeqIO.parse(sequences, 'fasta'):
    seq_list.append(str(record.seq))

top_seq = ''
total_results = []

A, T, C, G = 'A: ', 'T: ', "C: ", "G: "

for index in range(len(seq_list[1])):
    column = []
    for i in range(len(seq_list)):
        counter = 0
        column.append(seq_list[i][index])

    results = {"A": column.count("A"), "T": column.count("T"), "C": column.count("C"), "G": column.count("G")}
    top_seq += max(results, key=results.get)

    A = A + str(results["A"]) + ' '
    T = T + str(results["T"]) + ' '
    C = C + str(results["C"]) + ' '
    G = G + str(results["G"]) + ' '

print(top_seq)
print(A)
print(C)
print(G)
print(T)
