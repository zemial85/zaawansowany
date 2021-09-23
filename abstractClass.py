from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs

    @abstractmethod
    def move(self):
        pass


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, 4)

    def move(self):
        print("Walk")

    def speak(self):
        print("Woof,  Woof")

    def legs(self):
        print("Four paws")



class Fish(Animal):
    def __init__(self, name):
        super().__init__(name, 0)

    def move(self):
        print("Swim")

    def speak(self):
        print("Boolb,  Boolb")

    def legs(self):
        print("Four Fins")


class Bird(Animal):
    def __init__(self, name):
        super().__init__(name, 2)

    def move(self):
        print("Fly")

    def speak(self):
        print("Kraa, Kraa")

    def legs(self):
        print("Two legs and two wings")


dog = Dog("Pluto")
print(dog)
dog.move()
dog.speak()
dog.legs()
print("")

fish = Fish("Nemo")
print(fish)
fish.move()
fish.speak()
fish.legs()
print("")

bird = Bird("RoadRunner")
print(bird)
bird.move()
bird.speak()
bird.legs()