import csv


with open('ford_escort.csv') as file:
    data = csv.reader(file)
    print(data)

    data_list = list(data)

suma = 0
for row in data_list[1:]:
    suma += float(row[2])

print(suma/len(data_list) - 1)


