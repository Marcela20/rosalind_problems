import Utils

seq_list = Utils.loadSeqsFromFile("rosalind_grph.txt", "fasta")


def motifs(seq_1, seq_2):
    seqs = []
    for i in range(len(seq_1)):
        counter = 0
        sequence = ''
        j = 0
        while j < len(seq_2):

            if i + counter < len(seq_1):
                if seq_1[i + counter] == seq_2[j]:
                    sequence += seq_2[j]
                    counter += 1

                    if len(sequence) >= 2:
                        seqs.append(sequence)
                else:
                    sequence = ''
                    j -= counter
                    counter = 0

            else:
                break
            j += 1
    return seqs


final_results = []

for sequence_a in range(len(seq_list) - 1):
    results = motifs(seq_list[sequence_a].seq, seq_list[sequence_a + 1].seq)
    final_results.append(results)

res = set(final_results[0])
for x in final_results[1:]:
    res.intersection_update(x)

print(max(list(res), key=len))
