

import itertools

symbols = "A B C D E F G H".replace(" ", "")

def lista():
    my_list = list(itertools.product(symbols, repeat=6))
    lista = []
    for i in my_list:
        my_string = "".join(map(str, i))
        lista.append(my_string)
    return lista, len(lista)

print(lista())




