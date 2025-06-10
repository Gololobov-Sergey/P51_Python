# 000001 - 999999
# s = 0
# for i in range(1, 1000000):
#     n6 = i % 10
#     n5 = i // 10 % 10
#     n4 = i // 100 % 10
#     n3 = i // 1000 % 10
#     n2 = i // 10000 % 10
#     n1 = i // 100000
#     if n1 + n2 + n3 == n4 + n5 + n6:
#         s += 1
# print(s)


# s = 0
# for i in range(1, 50000):
#     n5 = i % 10
#     n4 = i // 10 % 10
#     n3= i // 100 % 10
#     n2 = i // 1000 % 10
#     n1 = i // 10000
#
#     if n1 == 4 or n2 == 4 or n3 == 4 or n4 == 4 or n5 == 4 or n1 == 1 and n2 == 3 or n2 == 1 and n3 == 3 or n3 == 1 and n4 == 3 or n4 == 1 and n5 == 3:
#         s += 1
# print(s)

# s = 0
# for i in range(10000, 100000):
#     k = 0
#     m = i
#     while m > 0:
#         r = m % 10
#         if r == 5:
#             k += 1
#         m //= 10
#     if k == 3 and i % 9 == 0:
#         s += 1
#         print(i, end=' ')
# print()
# print(s)

# c = 0
# for h in range(24):
#     h1 = h // 10
#     h2 = h % 10
#     for m in range(60):
#         m1 = m // 10
#         m2 = m % 10
#         for s in range(60):
#             s1 = s // 10
#             s2 = s % 10
#             if h1 == s2 and h2 == s1 and m1 == m2:
#                 print(h1, h2, ":", m1, m2, ":", s1, s2)
#                 c += 1
# print(c)

# for m in range(1, 10):
#     for n in range(1, 10):
#         print(m, "*", n, "=", m*n, end='   ')
#     print()

#
# for i in range(1, 100):
#     s1 = 0
#     for k in range(1, i):
#         if i % k == 0:
#             s1 += k
#     for j in range(i+1, 100):
#         s2 = 0
#         for k in range(1, j):
#             if j % k == 0 and k != i:
#                 s2 += k
#         if s1 == s2:
#             print(i, "  ", j)


# import random
# a = random.randint(1, 60)
# print(a)