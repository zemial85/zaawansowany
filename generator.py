def testowy_generator(generator):
    yield 'g'
    yield 'e'
    yield 'n'
    yield 'e'
    yield 'r'
    yield 'a'
    yield 't'
    yield 'o'
    yield 'r'


a = testowy_generator("generator")
#print(next(a))
#print(next(a))
#print(next(a))
#print(next(a))
#print(next(a))
#print(next(a))
#print(next(a))
#print(next(a))
#print(next(a))
#print(next(a))



for x in testowy_generator("generator"):
    print(x)

