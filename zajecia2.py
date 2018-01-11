def plus(a, b):
    return a + b


def minus(a, b):
    return a-b


def razy(a, b):
    return a * b


def dzielone(a, b):
    return a / b


def dwaNaDziesiec(liczba):
    dlugosc = len(str(liczba))
    wynik = 0
    for i in range(dlugosc):
        wynik *= 2
        wynik += int(liczba[i])
    print(wynik)


def dziesiecNaDwa(liczba, system):
    dzielna = int(liczba)
    wynik = ""
    while dzielna:
        wynik = str(dzielna % int(system)) + wynik
        dzielna = dzielna//int(system)
    print(wynik)


"""
print(plus(3, 4))
print(minus(3, 4))
print(dzielone(3,4))
print(razy(3,4)) 
"""
dziesiecNaDwa(4, 3)
n = "110"
dwaNaDziesiec(n)
