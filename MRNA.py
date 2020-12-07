prot_seq = open("rosalind_mrna (1).txt").read()

def rna_wariants(protein_sequence):
    nt1 = sum(map(protein_sequence.count, ["M", "W"]))
    nt2 = sum(map(protein_sequence.count, ["C", "D", "F", "E", "H", "K", "N", "Q", "Y"]))
    nt3 = sum(map(protein_sequence.count, ["I"]))
    nt4 = sum(map(protein_sequence.count, ["A", "P", "T", "V", "G"]))
    nt6 = sum(map(protein_sequence.count, ["R", "L", "S"]))
    result = 1 ** nt1 * 2 ** nt2 * 3 ** nt3 * 4 ** nt4 * 6 ** nt6 * 3
    return result % 1000000

print(rna_wariants(prot_seq))
