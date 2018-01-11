import os
import time
from random import randint


def wiosenny_deszczyk(kolumny, wiersze):
    #wygenerowanie miejsc dla "x"
    xlist = []
    for k in range(wiersze+1):
        xlist.append(randint(0,kolumny-1))
    print(xlist)

    n = 0
    while n < wiersze:
        os.system("cls")
        for j in range(n, -1, -1):
            print("o "*(int(xlist[j]))+"x "+"o "*(kolumny-1-int(xlist[j])))
        for i in range(n, wiersze-1):
            print("o "*kolumny)
        n += 1
        print("\n")
        time.sleep(0.3)


def rosnacy_kwadrat(wiersze,kolumny):
    srodek = [kolumny//2, wiersze//2]

    for k in range(-min(kolumny//2, wiersze//2), min(kolumny//2, wiersze//2)+1):
        os.system("clear")
        for i in range(kolumny):
            for j in range(wiersze):
              if max(abs(j-srodek[1]), abs(i-srodek[0])) == abs(abs(k)-abs(min(kolumny//2, wiersze//2))):
                  print("x ", end="")
              else:
                  print("o ", end="")
            print("")
        time.sleep(0.3)


wiosenny_deszczyk(11, 7)
#rosnacy_kwadrat(11,7)