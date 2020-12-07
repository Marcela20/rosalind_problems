import requests
from Bio import SeqIO

import Utils
import re

with open("rosalind_mprt (1).txt") as names:
    lines = names.readlines()

for name in lines:
    url = "http://www.uniprot.org/uniprot/" + name.rstrip() + ".fasta"
    r = requests.get(url, allow_redirects=True)
    a = open("sequences", "ab").write(r.content)

seq_list = Utils.loadSeqsFromFile("sequences", "fasta")

for index in range(len(seq_list)):
    seq_list[index].id = lines[index].rstrip()


def find_motif_2(seq_long):
    pattern = r'N(?=[^' + 'P' + ']  [^' + 'P' + '])'
    x = re.finditer(pattern, seq_long)
    matches_positions = [match.start() + 1 for match in x]
    patterns = [].append(pattern)
    return matches_positions


for tmp in seq_list:
    if find_motif_2(str(tmp.seq)) != []:
        print(tmp.id)
        print(*find_motif_2(str(tmp.seq)), sep=", ".replace(",", ""))
