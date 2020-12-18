forward = 'tggaatgttgataaaagtaatgccccacctacctatactctttca'.upper()
reverse = 'tggaatgttgataaaagtaatgccccacctacctatactctttca'.upper()

ready_rev = reverse[::-1].translate(str.maketrans("ATGC", "TACG"))

print("starter reverse: ", ready_rev.lower())


def GC_content(primer):
    zaw_GC = 0
    proc_mut = (3 * 100) / len(primer)
    for i in primer:
        if i == 'G' or i == 'C':
            zaw_GC += 1
    Tm: int = 2 * (len(primer) - zaw_GC) + 4 * zaw_GC
    Tm_mut_sub: int = 81.5 + (0.41 * (zaw_GC * 100) / len(primer)) - (675 / len(primer)) - proc_mut

    return (zaw_GC * 100) / len(primer), len(primer), Tm, Tm_mut_sub


print("dla forward: ", GC_content(forward.upper()))
print("dla reverse: ", GC_content(ready_rev.upper()))
