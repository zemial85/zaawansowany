class MinusError(Exception):
    pass


class PositiveNumbers:
    def __init__(self):
        self.numbers = []

    def add_numbers(self, number):
        if number > 0:
            self.numbers.append(number)
            return self.numbers
        else:
            raise MinusError("wrong numbers")

    def clean_list(self):
        self.numbers = []
        return self.numbers

    def __iter__(self):
        return iter(self.numbers)

    def __str__(self):
        return f"{self.numbers}".format(self=self)



positive_numbers = PositiveNumbers()
positive_numbers.add_numbers(5)
positive_numbers.add_numbers(1)
print(positive_numbers.numbers)
#positive_numbers.clean_list()
print(positive_numbers.numbers)

for number in positive_numbers:
    print(number)

print(positive_numbers)







