import random


class CustomIterDict():
    def __init__(self, begin, end, division):
        if begin%2 == 0:
            self.begin = begin
        else:
            self.begin = begin + 1
        self.end = end
        self.division = division

    def __iter__(self):
        return self

    def __next__(self):
        if self.begin >= self. end:
            raise StopIteration
        else:
            stan = self.begin
            self.begin += self.division
            return stan


custom = CustomIterDict(0, 10, 2)

for number in custom:
    print(number)




