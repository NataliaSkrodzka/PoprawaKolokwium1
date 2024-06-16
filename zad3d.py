def dswieListy(nazwa_pliku):
    plik=open(nazwa_pliku)
    line=plik.readline()
    plik.close()
    print(line)
    liczby=line.split(' ')
    print(liczby)
    listaBezPowtorzen=list(dict.fromkeys(liczby))
    print(listaBezPowtorzen)
    listaIloscWystapien=[]
    for i in listaBezPowtorzen:
        k=0
        for j in liczby:
            if i==j:
                k+=1
        listaIloscWystapien.append(k)
    print(listaIloscWystapien)

print(dswieListy('liczby.txt'))