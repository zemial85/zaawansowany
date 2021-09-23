import ast
import json
import random
from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, login):
        self.login = login
        self.hp = 100
        self.iq = 10
        self.strength = 10

    @abstractmethod
    def attack(self):
        pass

class Mag(Character):
    def __init__(self, login, strength_m=20, iq_w=20, hp_w=80):
        super().__init__(login)
        self.strength_m = strength_m + random.randint(-5, 5)
        self.iq_w = iq_w + random.randint(-5, 5)
        self.hp_w = hp_w + random.randint(-5, 5)
        print(f"login: {self.login} iqw: {self.iq_w} hpw: {self.hp_w}")

    def attack(self):
        print(f"missed: {self.login} iqr: {self.iq_w}")

    def damage(self):
        print(self.iq_w + self.iq_w)

class Dwarf(Character):
    def __init__(self, login, strength_d=30, iq_d=5, hp_d=200):
        super().__init__(login)
        self.iq_d = iq_d + random.randrange(-5, 5)
        self.hp_d = hp_d + random.randrange(-5, 5)
        self.strength_d = strength_d + random.randrange(-5, 5)
        self.strength_r = random.randrange(-5, 5)
        print(f"login: {self.login} iqd: {self.iq_d} hpd: {self.hp_d} strengthd: {self.strength_d}")

    def attack(self):
        print(f"missed: {self.login} strengthd: {self.strength_r}")

    def damage(self):
        print(self.strength_d + self.strength_r)

class Team(Character):
    def __init__(self, login, hp_t=150, strength_t=33):
        super().__init__(login)
        self.postac = []
        self.hp_t = hp_t + random.randrange(-5, 5)
        self.strength_t = strength_t + random.randrange(-5, 5)
        print(f"login: {self.login} hp_t: {self.hp_t} strength_t {self.strength_t}")

    def dodaj_krasnoluda(self, krasno):
        self.postac.append(f"'postac': {krasno}, 'nazwisko': {self.hp_t + random.randrange(-5, 5)}")

    def attack(self):
        pass


mag1 = Mag('Gandalf')
mag1.attack()
mag1.damage()

print('Wizard: ', mag1.__dict__)
print('++++++++++++++++++++++++')

dwarf = Dwarf('Dain')
dwarf.attack()
dwarf.damage()

print('Dwarf: ', dwarf.__dict__)
print('**************************')

team = Team('Krasnoludy')
team.attack()
team.dodaj_krasnoluda('mag1')
team.dodaj_krasnoluda('mag2')
team.dodaj_krasnoluda('mag3')
team.dodaj_krasnoluda('mag4')
team.dodaj_krasnoluda('mag5')

for krasn in team.postac:
    print(krasn)

with open("kursanci.json", 'w') as out_file:
    json.dump(team.postac, out_file, indent=0)
print('----------------------------------------')

with open("kursanci.json") as in_file:
    data = json.load(in_file)
    for even in data:
        print(even)

for i in even['postac']:
    print(i['postac'])