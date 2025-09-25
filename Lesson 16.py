import random


def num(n):
    print(n, end=' ')
    if n > 1:
        num(n-1)


def num2(n):
    if n > 1:
        num2(n-1)
    print(n, end=' ')



# num2(5)

def sum(a, b):
    if a == b:
        return a
    return a + sum(a+1, b)

# print(sum(1,10))

def pow(a, n):
    if n == 1:
        return a
    return a * pow(a, n-1)

# print(pow(2,8))


from function import *

# printLine(20)


def minSumma(list_, index, minIndex, minSum):
    if index + 10 > len(list_):
        return minIndex

    currentSum = 0
    for i in range(10):
        currentSum += list_[i + index]

    if currentSum < minSum:
        minIndex = index
        minSum = currentSum

    return minSumma(list_, index + 1, minIndex, minSum)

list_ = [random.randint(1,5) for i in range(100)]
# print(list_)
# print(minSumma(list_, 0, 0, 99999999))


def countNum(n):
    if n == 0:
        return 0
    return n % 10 + countNum(n//10)

# print(countNum(1411))


def fibo(n):
    if n == 1 or n == 2:
        return 1
    return fibo(n-1) + fibo(n-2)

print(fibo(6))


a = 55
a = fibo
# print(a(5))

list_ = [random.randint(1,50) for i in range(20)]


def asc(a, b):
    return a > b

def desc(a, b):
    return a < b


def evenFirst(a, b):
    if a % 2 == 0 and b % 2 == 1:
        return False
    if a % 2 == 1 and b % 2 == 0:
        return True
    return asc(a, b)

def bubbleSort(list_, method = asc):
    for i in range(len(list_) - 1):
        for j in range(len(list_) - 1 - i):
            if method(list_[j], list_[j+1]):
                list_[j], list_[j+1] = list_[j+1], list_[j]

print(list_)
bubbleSort(list_)
print(list_)