# st1 = 'mama'
# print(st1)
#
# print(st1[2])
#
# st2 = "papa"
# st3 = st1 + " " + st2
# print(st3)
#
# print(st3[1:8:2])
# print(st3[::-1])


# st1 = 'mama papa Baba' #input()
# st4 = "M" + st1[1:]
# print(st4)

# print(st1.find('a'))
# print(st1.rfind('a'))

# l = ['1','2','3','4','5']
#
# print("-".join(l))
#
# print(st1.count('am'))
# print(st1.capitalize())
# print(st1.title())
# print(st1.index('a'))
# print("3".isalnum())
# print(st1.isupper())
#
# print(st1.upper())
# print(st1.lower())

# print(st1.replace('a', 'o', 2))
# print(st1.split('a'))
# print(st1.startswith('m'))
# print(st1.endswith('m'))
# print(st1.ljust(20), end=' ')
# print("wwwwww")
# print(st1.rjust(20))
# print(st1.center(20))
#
# print("123".zfill(20))

st = "мама мила раму2222222 на дачі 123 рази"

st1 = st.split()
st1.reverse()
# print(" ".join(st1))
# print(len(st.split()))
# l = [4,4,4,2,4,3,4]
# l1 = [len(i) for i in st.split()]
# print(l1)
# print(sum(l1) / len(st.split()))

# Користувач вводить з клавіатури рядок. Порахуйте кількість
# букв, цифр у рядку. Виведіть обидві кількості на екран.

# l = 0
# d = 0
# for s in st:
#     if s.isalpha():
#         l += 1
#     if s.isdigit():
#         d += 1
# print(l, d)

# Користувач вводить із клавіатури рядок. Знайдіть найдовше слово в
# рядку і виведіть його на екран. Якщо таких слів декілька, виведіть перше з них.

l1 = [len(i) for i in st.split()]
print(st.split()[l1.index(max(l1))])