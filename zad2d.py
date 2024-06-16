import random

def randomowaLista(min, max, ile):
    try:
        if min > max or ile < 1:
            raise ValueError
        lista = random.sample(range(min, max), ile)
        print(lista)
        slownik={}
        for i in range(len(lista)):
            slownik[lista[i]]=i
        return slownik
    except ValueError:
        print("min musi byc mniejszy niz maz a ile musi byc wieksze od 0.")


print(randomowaLista(0,9,5))

