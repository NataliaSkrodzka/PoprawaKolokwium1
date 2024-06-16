import random

def listaRandom(min, max, ile):
    lista =[random.randint(min, max) for _ in range(ile)]
    print(lista)
    print(lista[0::2])


listaRandom(1,9,7)