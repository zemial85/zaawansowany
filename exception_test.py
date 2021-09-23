
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj druga liczbe: "))

try:
    print(a/b)

except ZeroDivisionError:
    print("Nie dzielimy przez zero")

