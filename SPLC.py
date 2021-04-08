from Bio.Seq import Seq
import Utils
sequences = Utils.loadSeqsFromFile("splicing", 'fasta')



def splicing():
    main_seq = str(sequences[0].seq)
    for i in range(1, len(sequences)):
        if str(sequences[i].seq) in main_seq:
            main_seq = main_seq.replace(str(sequences[i].seq), "")
    return main_seq


mRNA = Seq(splicing())

print(mRNA.translate().rstrip("*"))