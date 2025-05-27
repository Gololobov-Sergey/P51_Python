# f1 = 1
# f2 = 1
# n = int(input("n = "))
# k = 2
# while k < n:
#     fn = f1 + f2
#     f1 = f2
#     f2 = fn
#     k += 1
#     print(fn, end = ' ')


# Спортсмен-лыжник начал тренировки, пробежав в первый день 10 км.
# Каждый следующий день он увеличивал длину пробега на P процентов от
# пробега предыдущего дня (P — ціле, 0 < P < 50). По данному P
# определить, после какого дня суммарный пробег лыжника за все дни пре-
# высит 200 км, и вывести найденное количество дней K (целое) и суммар-
# ный пробег S (вещественное число).

# s0 = 10
# d = 1
# s = 10
# p = 50
# while s <= 200:
#     sd = s0 * p / 100 + s0
#     d += 1
#     s += sd
#     s0 = sd
#
# print(d)
# print(s)


# a = 1
# while a < 5:
#     print(a)
#     if a == 3:
#         break
#     a += 1

# v = 4
# n = 2
# l = 12
# s = 0
# k = 0
# while s < l:
#     s += v
#     k += 1
#     if s >= l:
#         pass
#     else:
#         s -= n
# print(k)


# a = 1
# s = 0
# while a != 0:
#     a = int(input())
#     s += a
#
# print(s)


# for i in range(10):
#     print(i)

# n = int(input("Скільки є магазинів : "))
# s = 0
# for m in range(1, n+1):
#     h = int(input(f"Скількі є холодильників в магазині №{m} : "))
#     s += h
# print(s)

# sh1000 = 0
# n = int(input())
# for i in range(n):
#     u = int(input())
#     if u > 1000:
#         sh1000 += 1
#
# print(sh1000)

a = 11
b = 30
for i in range(a, b+1):
    if i % 2 == 0:
        print(i)