class HouseError(Exception):
    pass

class House:
    def __init__(self, colour):
        self.number = 1564
        self.roofColour = colour


    def dachowki(self):
        print(self.roofColour)


class FamilyHouse(House):
    def __init__(self):
        super().__init__(self, colour)




h = House("red")
print(h)
print(h.number)
print(h.roofColour)


print(h.dachowki())



