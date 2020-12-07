forward = 'gatgcttcgaaatacgaaacgtggcagt'.upper()
reverse = 'gccatagctttgtgtcattgatcatacc'.upper()

ready_rev = []

for i in reverse:
    if i == 'A':
        ready_rev.append('T')
    elif i == 'T':
        ready_rev.append('A')
    elif i == 'C':
        ready_rev.append('G')
    elif i == 'G':
        ready_rev.append('C')
    else:
        ready_rev.append('?')

ready_rev = ''.join(ready_rev)

print(ready_rev[::-1].lower())


def GC_content(primer):
    zaw_GC = 0
    for i in primer:
        if i == 'G' or i == 'C':
            zaw_GC += 1
    Tm: int = 2 * (len(primer) - zaw_GC) + 4 * zaw_GC

    return (zaw_GC * 100) / len(primer), len(primer), Tm

print(GC_content(forward.upper()))
print(GC_content(ready_rev.upper()))