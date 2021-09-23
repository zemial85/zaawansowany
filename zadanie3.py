from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, name, hp, intelligence, strength):
        self.name = name
        self.hp = hp
        self.intelligence = intelligence
        self.strength = strength

    @abstractmethod
    def attack(self):
        pass


class Wizard(Character):
    def __init__(self, name):
        super().__init__(name, 80, 20, 10)

    def attack(self):
        print(f"{self.name} hits with fireball for {self.intelligence} Dp")
        pass


class Dwarf(Character):
    def __init__(self, name):
        super().__init__(name, 200, 5, 30)

    def attack(self):
        print(f"{self.name} hits with hammer for {self.strength} Dp")
        pass


wizard = Wizard("Gandalf")
dwarf = Dwarf("Dain")

wizard.attack()
dwarf.attack()

