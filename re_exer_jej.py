import re


with open("/home/daniel/PycharmProjects/zaawansowany/nazwy.txt") as file:
    data = file.read()



print(re.findall(".+\.py", data))

a = re.finditer(".+\.py", data)
for x in a:
    print(x)

print(re.search(".+\.py", data))