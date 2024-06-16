def sumaBitow(imie, nazwisko, a):
    b=len(imie)
    c=len(nazwisko)
    wynik=a*(b+c)
    print(wynik)
    wynikBin = bin(a * (b + c))
    print(wynikBin)
    k=0
    for i in range(len(wynikBin)):
        if wynikBin[i] == '1':
            k+=1
    return k



print(sumaBitow("Natali", "Skrodzka", 2))
