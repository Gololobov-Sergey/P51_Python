# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# d = int(input("d = "))
# s = 0
import random

# l = [2.365, True, "2345", 2134]
#
# for i in range(4):
#     print(l[i])


# list1 = [random.randint(1, 10) for i in range(10)]
# print(list1)
# iMax = 0
# iMin = 0
# for i in range(len(list1)):
#     if list1[i] > list1[iMax]:
#         iMax = i
#     if list1[i] < list1[iMin]:
#         iMin = i
#
# s = 0
# if iMin > iMax:
#     t = iMax
#     iMax = iMin
#     iMin = t
# for i in range(iMin + 1, iMax):
#     s += list1[i]
# print(s)


list1 = [random.randint(1, 10) for i in range(10)]
print(list1)

list2 = [elem for elem in list1 if elem % 3 == 0]
print(list2)

print(min(list1))
print(max(list1))
print(sum(list1))


# list1.insert(0, 44)
# list1.insert(1, 55)
# list1.append(99)
# list1.remove(44)
# print(list1.index(9))

# for i in range(len(list1)-1,-1,-1):
#     print(list1[i], end=' ')
# print()
# print(list1)

# t = list1[0]
# list1[0] = list1[len(list1)-1]
# list1[len(list1)-1] = t

# for i in range(len(list1)//2):
#     list1[i], list1[len(list1)-1-i] = list1[len(list1)-1-i], list1[i]
#
# print(list1)
#
# list1.reverse()
# print(list1)


# maxValue = list1[0]
# for elem in list1:
#     if elem > maxValue:
#         maxValue = elem
# print(maxValue)
#
# iMax = 0
# for i in range(len(list1)):
#     if list1[i] > list1[iMax]:
#         iMax = i
# print(iMax)



