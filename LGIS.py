import itertools
from console_progressbar import ProgressBar

pb = ProgressBar(total=100, prefix='Here', suffix='Now', decimals=3, length=50, fill='X', zfill='-')

with open("rosalind_lgis.txt", "r") as file:
    data = file.readlines()
print('file opened')
# data = open("rosalind_lgis.txt", "r").readlines()

sequence_int = list(map(int, data[1].split(" ")))
print('sequence list done ')
my_list_1 = []
my_list_2 = []


def lgis(data_set, data_set_len):
    print(len(data_set))
    lista_a = []
    for n in range(8000, data_set_len):
        lista_a = list(itertools.combinations(data_set, n))
        print(lista_a)
        print(pb.print_progress_bar((n * 100 / data_set_len)))

        for a in lista_a:
            if a == tuple(set(a)):
                my_list_1.append(a)
            if a == tuple(set(a))[::-1]:
                my_list_2.append(a)

    print(my_list_1)
    print(my_list_2)
    listToStr_1 = ' '.join([str(elem) for elem in max(my_list_1, key=len)])
    listToStr_2 = ' '.join([str(elem) for elem in max(my_list_2, key=len)])
    print(listToStr_1)
    print(listToStr_2)
    return lista_a


lista = lgis(sequence_int, int(data[0]))
