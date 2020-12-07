allels_a = ["AA", "Aa", "aa"]
allels_b = ["BB", "Bb", 'bb']
gamets = []
genotypes = []
for x in allels_a:
    for y in allels_b:
        genotypes.append(x + y)
print(genotypes)

for genotype in genotypes:
    ala = []
    alb = []
    genotypekeeper = []
    for i in genotype:
        if i == "a" or i == "A":
            ala.append(i)
        else:
            alb.append(i)
    for a in ala:
        for b in alb:
            genotypekeeper.append(a+b)
    gamets.append(genotypekeeper)
print(gamets)

mate = ['AB', 'Ab', 'aB', 'ab']
for x in gamets:
    genotype_ost = []
    lista = []
    for gamet in x:
        for gamet_mate in mate:
            genotype_ost.append(gamet+gamet_mate)
    for i in genotype_ost:

        if i.count("A") == 1 and i.count("B") == 1:
            lista.append(i)
    print(len(lista)/16)

