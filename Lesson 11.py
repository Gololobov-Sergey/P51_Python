import random

# size = int(input("size = "))
# list1 = [int(input(f"list[{i}] = ")) for i in range(size)]
# # for i in range(size):
# #     list1.append(int(input(f"list[{i}] = ")))
#
# print(list1)

# temperature = [random.randint(10, 30) for i in range(24)]
# print(temperature)
#
# for i in range(30):
#     for h in range(24):
#         if 30-i > temperature[h]:
#             print("   ", end='')
#         else:
#             print("*  ", end='')
#     print()
#
# deltaMax = 0
# for i in range(len(temperature) - 1):
#     delta = abs(temperature[i+1] - temperature[i])
#     if delta > deltaMax:
#         deltaMax = delta
#         h = i
# print(h)


# list1 = [random.randint(10, 30) for i in range(10)]
# print(list1)
# for i in range(len(list1) - 1):
#     for j in range(len(list1) - 1 - i):
#         if list1[j] < list1[j+1]:
#             list1[j], list1[j+1] = list1[j+1], list1[j]
#
# print(list1)


list1 = [[1,2,3], [4,5,6], [4,6,8]]
for i in range(len(list1)):
    s = 0
    for j in range(len(list1[i])):
        print(list1[i][j], end=' ')
        s += list1[i][j]
    print(f" | {s}")

for j in range(len(list1[0])):
    s = 0
    for i in range(len(list1)):
        s += list1[i][j]
    print(s, end =" ")




