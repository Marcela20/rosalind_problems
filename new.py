import itertools

with open("rosalind_lgis.txt", "r") as file:
    data = file.readlines()


sequence_int = list(map(int, data[1].split(" ")))
my_list_1 = []
my_list_2 = []

def lgis(data_set, data_set_len):
    lista_a = []
    for n in range(2, data_set_len+1):
        lista_a += list(itertools.combinations(data_set, n))
        print(lista_a)

    for a in lista_a:
        if a == tuple(set(a)):
            my_list_1.append(a)
        if a == tuple(set(a))[::-1]:
            my_list_2.append(a)

    # print(my_list_1)
    # print(my_list_2)
    listToStr_1 = ' '.join([str(elem) for elem in max(my_list_1, key=len)])
    listToStr_2 = ' '.join([str(elem) for elem in max(my_list_2, key=len)])
    print(listToStr_1)
    print(listToStr_2)
lista = lgis((7, 5, 1, 4, 2, 3, 6), 7)#int(data[0]))