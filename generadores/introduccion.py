
#todo los generadores son como una fabrica que cada vex que yo necesita un dulce en vez de darme todos ala vez nos da uno por uno 

def generadora():
    yield 1
    yield 2
    yield 3 #todo oucpamos la parral yield para darle algo 
    yield 4
    yield 5

generador= generadora()
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
