
from Bio.Seq import Seq

rna = open("").read()
rna = Seq(rna, generic_rna)
print(rna.translate())
