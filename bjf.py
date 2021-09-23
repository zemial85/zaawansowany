# Type your code here:
from math import pi


def circle_perimeter(radius):
        p = 2 * pi * radius
        return p

# You don't need to modify the follwoing part
# it allows you to test your code before submitting it:

if __name__ == "__main__":
    print(circle_perimeter(10))


def print_even_numbers(start, stop):
    for i in range(start, stop):
        if (i % 2 == 0):
            print(sum(i))


print_even_numbers(0, 100)