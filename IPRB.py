k, m, n = 24, 26, 18

def mendel(k, m, n):
    populacja = k + m + n
    populacja_2 = populacja - 1

    pm, pn, pk = m/(k+m+n), n/(k+m+n), k/(k+m+n)

    lista_początkowa = [pk, pm, pn]

    lista_k = [(k - 1) / populacja_2, n / populacja_2, m / populacja_2]
    lista_m = [k / populacja_2, n / populacja_2, (m - 1) / populacja_2]
    lista_n = [k / populacja_2, (n - 1) / populacja_2, m / populacja_2]

    lista_koncowa = [lista_k, lista_m, lista_n]

    lista_ostateczna = zip(lista_początkowa, lista_koncowa)

    prawdop_lista = []

    for i, y in lista_ostateczna:
        prawdop = []
        for z in y:
            prawdop.append(i*z)
        prawdop_lista.append(prawdop)

    return prawdop_lista

prawd_k = [1, 1, 1]
prawd_m = [1, 0.5, 0.75]
prawd_n = [ 1, 0, 0.5]

print(mendel(k, m, n))

prawdopodobieństwa = mendel(k, m, n)



prawd_sum = [prawd_k, prawd_m, prawd_n]

listapokrzyzowaniu = zip(prawdopodobieństwa, prawd_sum)
#print(tuple(listapokrzyzowaniu))

wynik_ostateczny_z_ostatnich = 0
for x, y in listapokrzyzowaniu:
    for i in range(3):
        wynik_ostateczny_z_ostatnich += x[i] * y[i]

print(wynik_ostateczny_z_ostatnich)
# print(tuple(listapokrzyzowaniu))