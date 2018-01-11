def iter_silnia(n):
    wynik = 1
    if n == 0:
        return wynik
    else:
        for i in range(1, n+1):
            wynik = wynik * i
    return wynik


def reku_silnia(n):
    if n < 2:
        return 1
    else:
        return n*reku_silnia(n-1)


def iter_fibonacci(n):
    a = 0
    b = 1
    c = 1
    if n == 0:
        return 0
    else:
       for i in range(2, n):
            a = b
            b = c
            c = a + b
       return c


def reku_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return reku_fibonacci(n-1)+reku_fibonacci(n-2)

# pokombinuj jeszcze z tym
def pascal(n, k):
    if k == 0 or k == n:
        return 1
    return pascal(n - 1, k - 1) + pascal(n - 1, k)

for i in range(8):
    for j in range(i + 1):
        print(pascal(i, j), end=' ')
    print()
#print(iter_silnia(11))
#print(reku_silnia(11))
#print(reku_fibonacci(19))
#print(iter_fibonacci(0))