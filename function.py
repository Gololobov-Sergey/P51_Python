def printLine(symbol = '*', count = 20, isVerical = True):
    for i in range(count):
        print(symbol, end='')
        if isVerical:
            print()
    print()


def plus(a, b):
    c = a + b
    return c

def isEven(a):
    return a % 2 == 0


def max4(a, b, c, d):
    max = a
    if b > max:
        max = b
    if c > max:
        max = c
    if d > max:
        max = d
    return max


def isPrime(a):
    for i in range(2, a):
        if a % i == 0:
            return False
    return True


def happynum(a):
    n6 = a % 10
    n5 = a // 10 % 10
    n4 = a // 100 % 10
    n3 = a // 1000 % 10
    n2 = a // 10000 % 10
    n1 = a // 100000
    return n6 + n5 + n4 == n3 + n2 + n1


def printList(list_):
    for el in list_:
        print(el, end=' ')
    print()


def countSymbol(n):
    return len(str(n))
    # if n == 0:
    #     return 1
    # count = 0
    # if n < 0:
    #     n = abs(n)
    #     count = 1
    # while n > 0:
    #     count += 1
    #     n //= 10
    # return count

def countSymbolList(list_):
    count = 0
    for el in list_:
        count += countSymbol(el)
    return count

def prinListInStarLine(list_):
    count = countSymbolList(list_) + len(list_) - 1
    printLine('*', count, False)
    printList(list_)
    printLine('*', count, False)