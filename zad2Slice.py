import random

def listaRandom(min, max, ile):
    try:
        if min>max or ile<=0:
            raise ValueError
        lista =[random.randint(min, max) for _ in range(ile)]
        print(lista)
        print(lista[0::2])
    except ValueError:
        print('ile musi byc wieksze od 0 a min musi byc mniejszy niz max')




listaRandom(2,1,9)