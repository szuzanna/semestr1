import re
import string

"""funkcja przygotowujaca napis"""


def przygotuj(tekst):
    return re.sub("[^a-zA-Z]+", "", tekst.lower())


def cezar(tekst, p):
    tekst = przygotuj(tekst)
    str = ""

    lista = [ord(c) for c in tekst]
    for i in range(len(lista)):
        if lista[i]+p > 122:
            lista[i] = (lista[i]+p) % 122 + 96
        else:
            lista[i] += p
    lista = [chr(c) for c in lista]

    return str.join(lista)


def brutus(kod, p):
    str = ""

    lista = [ord(c) for c in kod]
    for i in range(len(lista)):
        if lista[i] - p < 97:
            lista[i] = (lista[i] - p) + 26
        else:
            lista[i] -= p
    lista = [chr(c) for c in lista]

    return str.join(lista)


def podstawieniowy(tekst, alfabet):
    tekst = przygotuj(tekst)
    lista = [ord(c) for c in tekst]
    litery = [c for c in alfabet]

    for i in range(len(tekst)):
        lista[i] = litery[lista[i]-97]
    return "".join(lista)  # równoważne zapisowi z cezara


def dePodstawieniowy(kod, alfabet):
    lista = [c for c in kod]
    litery = [c for c in alfabet]

    for i in range(len(lista)):
        for j in range(len(litery)):
            if lista[i] == litery[j]:
                lista[i] = chr(j + 97)
                break  # po jednokrotnym wywołaniu tego warunku nie moze sprawdzać dłuzej
    return "".join(lista)


def zKluczem(tekst, klucz):
    lista = list(tekst)
    litery = list(klucz)
    dlugosc = len(klucz)

    for i in range(len(lista)):
        zamiana = (ord(litery[i % dlugosc]) - 96 + ord(lista[i]))
        if zamiana > 122:
            lista[i] = chr(zamiana % 122 + 96)
        else:
            lista[i] = chr(zamiana)
    return "".join(lista)


def deZKluczem(kod, klucz):
    lista = list(kod)
    litery = list(klucz)
    dlugosc = len(klucz)

    for i in range(len(lista)):
        zamiana = (ord(lista[i]) - ord(litery[i % dlugosc]) + 122)
        if zamiana > 122:
            lista[i] = chr(zamiana % 122 + 96)
        else:
            lista[i] = chr(zamiana)
    return "".join(lista)


#dane = input()
#print(przygotuj(dane))
#cos = cezar(dane, 2)
#print(cos)
#print(brutus(cos, 2))
#pacze = podstawieniowy("abpyz", "cdefghijklmnopqrstuvwxyzab")
#print(pacze)
#print(dePodstawieniowy(pacze, "cdefghijklmnopqrstuvwxyzab"))


ostatni = zKluczem("zaaaaa", "abz")
print(ostatni)
print(deZKluczem(ostatni, "abz"))
