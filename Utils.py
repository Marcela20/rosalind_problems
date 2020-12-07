from Bio import SeqIO

def loadSeqsFromFile(Path):
    sequences = open(Path)
    seq_list = []

    for record in SeqIO.parse(sequences, "fasta"):
        seq_list.append(record)
    return seq_list
