from abc import ABC, abstractmethod


class Restaurant(ABC):

    @abstractmethod
    def cook_food(self):
        pass


class Sushi(Restaurant):
    def cook_food(self):
        print("Cook rice")


class Burgers(Restaurant):
    def cook_food(self):
        print("Grill meat")


class MuffinHouse(Restaurant):
    def cook_food(self):
        print("Bake muffins")



sushi = Sushi()
print(sushi)
sushi.cook_food()

burgers = Burgers()
print(burgers)
burgers.cook_food()

muffin = MuffinHouse()
print(muffin)
muffin.cook_food()
