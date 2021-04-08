k, m, n = 24, 26, 18

def mendel(k, m, n):
    population = k + m + n
    population_2 = population - 1

    pm, pn, pk = m/(k+m+n), n/(k+m+n), k/(k+m+n)

    starting_list = [pk, pm, pn]

    list_k = [(k - 1) / population_2, n / population_2, m / population_2]
    list_m = [k / population_2, n / population_2, (m - 1) / population_2]
    list_n = [k / population_2, (n - 1) / population_2, m / population_2]

    list_fin = [list_k, list_m, list_n]

    list_fin_fin = zip(starting_list, list_fin)

    list_prob = []

    for i, y in list_fin_fin:
        prawdop = []
        for z in y:
            prawdop.append(i*z)
        list_prob.append(prawdop)

    return list_prob

prawd_k = [1, 1, 1]
prawd_m = [1, 0.5, 0.75]
prawd_n = [ 1, 0, 0.5]

print(mendel(k, m, n))

probabilities = mendel(k, m, n)



prawd_sum = [prawd_k, prawd_m, prawd_n]

listapokrzyzowaniu = zip(probabilities, prawd_sum)
#print(tuple(listapokrzyzowaniu))

wynik_ostateczny_z_ostatnich = 0
for x, y in listapokrzyzowaniu:
    for i in range(3):
        wynik_ostateczny_z_ostatnich += x[i] * y[i]

print(wynik_ostateczny_z_ostatnich)
# print(tuple(listapokrzyzowaniu))