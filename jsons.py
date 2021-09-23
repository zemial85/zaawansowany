import json

a = {
    "hotel": {
        "rooms": [
            {"room-number": 100,
             "name": "Dor",
             "surname": "Gryffin",
             "class": 2,
             "price": 277,
             "breakfast": True
             },
            {"room-number": 101,
             "name": "Claw",
             "surname": "Raven",
             "class": 2,
             "price": 277,
             "breakfast": False
             },

            {"room-number": 102,
             "name": "Therin",
             "surname": "Sly",
             "class": 1,
             "price": 326,
             "breakfast": True
             },
            {"room-number": 103,
             "name": "Puff",
             "surname": "Huffle",
             "class": 2,
             "price": 277,
             "breakfast": False
             }
        ],
        "parking": {
            "location": "premium",
            "style": "covered",
            "price": 50
        }
    }
}

with open("example.json", "w") as plik:
    json_tekst = json.dumps(a)
    #print(json_tekst)
    plik.write(json_tekst)
    # json.dump(a, plik)

with open('example.json') as plik:
    dane_plik = plik.read()
    #print(dane_plik)
    slownik = json.loads(dane_plik)
    print(slownik)
    print(type(slownik))
    x = slownik.get("hotel")
    z = x.get("rooms")
    res = [sub['price'] for sub in z]
    print(res)
    bf = [sub['breakfast'] for sub in z]
    print(bf)
cena = 0
for room in slownik["hotel"]["rooms"]:
    print(room["price"])
    cena += room["price"]
    if room["breakfast"]:
        cena += 50

cena += slownik["hotel"]["parking"]["price"]
print(cena)

d = {"zaplata": cena}

with open("rachunek.json", "w") as plik:
    rachunek_json = json.dumps(d)
    plik.write(rachunek_json)



