class ManagerPlikow:
    def __init__(self, nazwa_pliku, mod):
        self.nazwa_pliku = nazwa_pliku
        self.mod = mod
        self.obiekt_plikowy = None

    def __enter__(self):
        print('jestem w enter')
        self.obiekt_plikowy = open(self.nazwa_pliku, self.mod)
        return self.obiekt_plikowy

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('jestem w exit')
        self.obiekt_plikowy.close()


print('jeszcze nieotwarte')
with ManagerPlikow('jestem_z_kontekstu.txt', 'w') as obsluguje_plik:
    print(obsluguje_plik)
    print('jestem we wcieciu!')
    obsluguje_plik.write('kontext managewr power!')
print('zamkniete')