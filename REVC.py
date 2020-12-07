DNA =list('CTTCTTCGTTCGTGGTGCTG')
RNA= []
for i in DNA:
    if i == 'A':
        RNA.append('T')
    elif i == 'T':
        RNA.append('A')
    elif i == 'C':
        RNA.append('G')
    elif i == 'G':
        RNA.append('C')
    else:
        RNA.append('?')

RNAA= ''.join(RNA)
print(RNAA[::-1])
