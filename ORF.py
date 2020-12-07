from Bio.Seq import Seq
from Utils import loadSeqsFromFile
import re

Seq_list = loadSeqsFromFile("ORF_file")
sequence = str(Seq_list[0].seq)

my_seq = Seq(sequence)
my_seq_rev = my_seq.reverse_complement()


def reggae(seque):
    pattern = '(?=(ATG(?:...)*?)(?:TAG|TGA|TAA))'
    seq_finder = re.findall(pattern, seque)
    for index in range(len(seq_finder)):
        seq_finder[index] = str(Seq(seq_finder[index]).translate())
    return seq_finder


lista = reggae(sequence)

for x in reggae(str(my_seq_rev)):
    lista.append(x)

ready = set(lista)
for x in ready:
    print(x)
