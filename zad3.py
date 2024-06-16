def najczestszyElement(nazwa_pliku):
    plik=open(nazwa_pliku)
    linia=plik.read()
    plik.close()
    liczby=linia.split(' ')
    slownik={}
    for i in liczby:
        k=0
        for j in liczby:
            if i==j:
                k+=1
        slownik[i]=k
    maks=0
    for i in slownik.values():
        if i>=maks:
            maks=i
    print("Najczesciej wystepujacy element:")
    for key, value in slownik.items():
        if value==maks:
            print(key)


najczestszyElement('liczby.txt')