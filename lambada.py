mordy = [
    {'name': 'Aragorn','kills': 17},
    {'name': 'Legolas','kills': 11},
    {'name': 'Gimli','kills': 5},
    {'name': 'Eowyn','kills': 9},
    {'name': 'Gandalf','kills': 11}
]

checker = lambda x: x["kills"]
print(sorted(mordy, key=checker))
