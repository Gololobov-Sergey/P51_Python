# a = 10
#
# def func(a):
#
#     a += 100
#     print(a)
#     #return a
#
# func(a)
# print(a)


# l = [1,2,3,4]
#
# def f1(l1):
#     l1[0] = 999
#
# f1(l)
# print(l)


def factorial(number):
    f = 1
    for i in range(1, number+1):
        f *= i
    return f

ln = [21,23,34,4,5]

# def factorialList(ln):
#     lf = []
#     for i in ln:
#         lf.append(factorial(i))
#     return lf

# lf = factorialList(ln)

# lf = [factorial(i) for i in ln]
# print(lf)


# def isFibonachi(number):
#     f1 = 1
#     f2 = 1
#     fn = 0
#     while fn < number:
#         fn = f1 + f2
#         f1 = f2
#         f2 = fn
#     return fn == number
#
# print(isFibonachi(20))
#
# lf = [i for i in ln if isFibonachi(i)]
# print(lf)


def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(fact(10))