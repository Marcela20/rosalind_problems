from Bio import SeqIO

sequences = open("datasets/rosalind_grph.txt")
seq_list = []

for record in SeqIO.parse(sequences, 'fasta'):
    seq_list.append(record)

def overlap(seq_1, seq_2, len_seq=3):
    seqs = ''
    for i in range(len(seq_1)):
        counter = 0
        if seq_1[i] == seq_2[0]:
            seqs += seq_1[i]
            counter += 1
            for j in range(1, len(seq_1) - i):
                if seq_1[i + j] == seq_2[j]:
                    seqs += seq_2[j]
                    counter += 1
                else:
                    seqs = ''
                    counter = 0
                    break
        if counter == len_seq:
            return seqs, counter


for sequence_a in seq_list:
    for sequence_b in seq_list:
        if sequence_a.id == sequence_b.id:
            pass
        else:
            result = overlap(sequence_a.seq, sequence_b.seq)
            if result != None:
                print(sequence_a.id, sequence_b.id)
