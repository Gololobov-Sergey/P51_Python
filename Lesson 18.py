# # l = ["mama", "papa", "baba"]
# f = open("text.txt", "w", encoding="utf8")
# f.write("Слава Україні!")
# # # f.writelines(l)
# f.close()
import random

# f = open("text1.txt", "r", encoding="utf8")
# s = f.read().split('. ')
# f.close()
#
# for r in range(len(s)):
#     s[r] = s[r].capitalize()
#
# f = open("text2.txt", "w", encoding="utf8")
# f.write(". ".join(s))
# f.close()


# print("мама".capitalize())


# l = [random.randint(1, 100) for i in range(10)]
# f = open("num.txt", "w")
# s = [str(i) for i in l]
# f.write(" ".join(s))
# # for i in l:
# #     f.write(f"{str(i)} ")
# f.close()

# f = open("num.txt", "r")
# s = f.read().split()
# f.close()
# # l1 = [int(i) for i in s]
# l1 = list(map(int, s))
# print(l1)
# lp = [str(i) for i in l1 if i % 2 == 0]
# with open("num1.txt", "w") as f:
#     f.write(" ".join(lp))


print(ord('Z'))
print(chr(ord('Z') + 1))

s = "maza"
a = ""
for i in range(len(s)):
    a += chr(ord(s[i]) + 1)
print(a)