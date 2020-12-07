
class ParaKrolikow( ):
    def __init__(self):
        self.czy_jest_maly = True
        self.ile_ma_latek = 1

    def reprodukuj(self):
        if self.czy_jest_maly == True:
            return False
        else:
            return True

    def urosnij(self):
        self.ile_ma_latek += 1
        if self.ile_ma_latek > 1:
            self.czy_jest_maly = False

def fib_kroliki_co_zemra( miesiace, dlugosc_zycia_pary ):

    ilosc_par = 1
    para_startowa = ParaKrolikow()
    lista_par_krolikow = []
    lista_par_krolikow.append(para_startowa)

    for miesiace in range(miesiace):
        print('Miesiąc: ', miesiace)
        młode = []

        for parka in lista_par_krolikow:
            if parka.reprodukuj():
                # print('nowy kroliczek w miesiacu:', miesiace)
                nowa_parka = ParaKrolikow()
                młode.append(nowa_parka)

        if len(młode) != 0:
            lista_par_krolikow += młode
            # print('mlode: ', młode)
            # print('lista po dodaniu: ', lista_par_krolikow )

        for parka in lista_par_krolikow:
            parka.urosnij()
            if parka.ile_ma_latek > dlugosc_zycia_pary:
                lista_par_krolikow.remove(parka)

    print(lista_par_krolikow)
    print(len(lista_par_krolikow))

fib_kroliki_co_zemra( 6, 3 )



