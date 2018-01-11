"""problem plecakowy nalezy posortowac wagi danego elementu od najbardziej opytmalnej,
nastepnie wedle tej listy "wkladać" odpowednie przedmioty w ten sposób otrzymamy naj wersje"""

from math import sqrt


def BubleSort(dane, wartosci):
    balagan = True
    length = len(dane)-1
    while balagan == True and length > 0:
        balagan = False
        for i in range(0, length):
            if dane[i]/wartosci[i] > dane[i + 1]/wartosci[i+1]:
                dane[i], dane[i + 1] = dane[i + 1], dane[i]
                wartosci[i], wartosci[i+1] = wartosci[i+1], wartosci[i]
                balagan = True
        length -= 1


def czyPierwsza(n):
    n = int(n)
    jest = True
    #print(n, int(sqrt(n)))
    if n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if (n % i) == 0:
            jest = False
    return jest

def ileJest(n, lista):
    ile = 0
    for i in range(len(lista)):
        if lista[i] == n:
            ile += 1
    return ile


def plecakowy(dlugosci, ceny, ilepodac):
    BubleSort(dlugosci, ceny)

    cena = 0
    i = 0
    while ilepodac != 0:
        if ilepodac >= dlugosci[i]:
            ilepodac -= dlugosci[i]
            cena += ceny[i]
        else:
            i += 1
    return cena


def wykreslanka(napis):
    lista = napis.split(" ")
    i = 0
    print(lista)
    print(len(lista))

    while i < len(lista):
        n = lista[i]
        ilosc = ileJest(n, lista)
        print(czyPierwsza(n), (ilosc % 2) == 1)

        if czyPierwsza(n) and ((ilosc % 2) == 1):
            for j in range(ilosc):
                lista.remove(n)
            i -= 1
        i += 1
    return lista

"""dlugosci = list(range(1, 11))
ceny = [1, 5, 8, 9, 10, 16, 17, 20, 24, 26]

ilepodac = int(input("podaj dlugosc preta "))
print("najnizsza cenat to: " + str(plecakowy(dlugosci, ceny, ilepodac)))"""

print(wykreslanka("5 7 4 18 3 7 5 1 2 12 7 13"))
