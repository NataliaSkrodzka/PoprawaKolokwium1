import random

def listaRandom(min, max, ile):
    lista =[random.randint(min, max) for _ in range(ile)]
    print(lista)
    lista1=[]
    i=0
    while i in range(len(lista)):
        if i%2 == 0:
            lista1.append(lista[i])
        i+=1
    return lista1

print(listaRandom(0,9,7))

