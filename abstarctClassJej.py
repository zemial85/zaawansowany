from abc import ABC, abstractmethod


class Zwierze(ABC):
    def __init__(self, imie, konczyny):
        self.imie = imie
        self.konczyny = konczyny

    @abstractmethod
    def poruszanie(self):
        pass


class Swinka(Zwierze):
    def __init__(self, name):
        super().__init__(name, 4)

    def poruszanie(self):
        print('biegne!')

    def glos(self):
        print(f'jestem {self.imie} chrum')


class Kaczka(Zwierze):
    def __init__(self, name):
        self.skrzydla = 2
        super().__init__(name, 2)

    def poruszanie(self):
        print('lece!')

    def glos(self):
        print(f'jestem {self.imie} kwa')


class Pajak(Zwierze):
    def __init__(self, name):
        super().__init__(name, 8)

    def poruszanie(self):
        print('tuptam')


swinka = Swinka('Pepe')
swinka.glos()
swinka.poruszanie()
print('=================')
kaczusia = Kaczka('Hyzio')
kaczusia.glos()
kaczusia.poruszanie()
print('=================')
pajak = Pajak('Parker')
pajak.poruszanie()