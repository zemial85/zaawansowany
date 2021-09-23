import pickle



with open("pickle2", "wb") as file:
    newList = [x for x in range(1, 100) if x < 11]
    print(newList)
    newList = pickle.dumps(newList)
    print(newList)
    file.write(newList)
print("zapisalem")

with open("pickle2", "rb") as file:
    #dane = pickle.load(file)
    newList = file.read()
    print(newList)
    dane = pickle.loads(newList)
    print(dane)