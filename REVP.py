import Bio.SeqIO
from Bio import SeqIO

seqence = ''
with open("seqw", "r") as handle:
    for record in SeqIO.parse(handle, "fasta"):
        seqence = seqence + record.seq

print(seqence)

# seqence = "TCAATGCATGCGGGTCTATATGCAT"
nuc_dict = {"A": "T", "T": "A", "C": "G", "G": "C"}

for i in range(len(seqence) - 3):
    counter = 4
    a = []
    while counter <= 12 and counter + i <= len(seqence):

        if nuc_dict[seqence[i]] == seqence[i + counter - 1]:
            seqence_pal = ''
            seqence_pal_comp_rev = ''
            seqence_pal = seqence[i: i + counter]

            for y in seqence_pal:
                seqence_pal_comp_rev = seqence_pal_comp_rev + nuc_dict[y]

            a.append(nuc_dict[seqence[i]])
            if seqence_pal == seqence_pal_comp_rev[::-1]:
                print(i + 1, len(seqence_pal_comp_rev))

        counter += 1


b = a.translate(str.maketrans("ATGC", "TACG"))

