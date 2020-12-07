class Urodziny():
    def __init__(self, imie_sol, lista_gosci, zakupy, tresc_zapr):
        self.imie_sol = imie_sol
        self.lista_gosci = lista_gosci
        self.zakupy= zakupy
        self.tresc_zapr = tresc_zapr

    def funk1(self):
        goscie = list(self.lista_gosci.keys())
        for i in goscie:
            print(i)

    def funk2(self):
        print("Zapraszam"+ self.imie+ "na urodziny")

    def wypierdalac(self):
        self.lista_gosci = {}
# ------------------------
urodziny_Kasi = Urodziny("Kasia", {"asia":"as@as", "ania":"an@an"}, 20, "xd")
urodziny_kuby = Urodziny( "Kuba", {} , 'zrobi', 'wypierdlac')

urodziny_kuby.lista_gosci = urodziny_Kasi.lista_gosci
urodziny_kuby.funk1()
print('------------------')
urodziny_kuby.wypierdalac()
urodziny_kuby.funk1()