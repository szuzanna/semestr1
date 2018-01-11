from math import sqrt
from random import randint


def trojkat(bok, wys):
    return bok*wys/2


def heron(a, b, c,):
    t = [a, b, c]
    sorted(t)
    ift[0] + t[1] < t[2]:
        print("Podane wartosci nie tworza trojkata")
    else:
        p=(a + b + c)/2
        return sqrt(p*(p-a)*(p-b)*(p-c))

def losuj():
    wygrana = False
    liczba = randint(0, 9)
    print(liczba)
    while  not wygrana :
        zgadywana = int(input("podaj liczbe z zakresu [0;9]\n"))
        if zgadywana == liczba:
            print("WYGRANA")
            wygrana = True
        elif zgadywana > liczba:
            print("Liczba zbyt duża\n")
        else:
            print("Liczba zbyt mała\n")

def choinka(n):
    for i in range(1, n+1):
        for j in range(1,i+2):
            print(" "*(n+1-j)+"*"*(2*j-1)+" "*((2*n)//2-j), end="\n")

print(trojkat(3,4))
print(heron(3,5,4))
#losuj()
choinka(3)