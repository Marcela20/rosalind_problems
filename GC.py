from Bio import SeqIO

my_seqs = open("rosalind_gc.txt")

highest_counter = 0

for record in SeqIO.parse(my_seqs, "fasta"):
    counter = 0
    counter += record.seq.count("G")
    counter += record.seq.count("C")
    print(record.id, counter)

    if highest_counter < counter:
        highest_counter = counter
        top = {(highest_counter * 100 / len(record.seq)): record.id}


print(top)


