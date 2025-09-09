# words = ['mama', 'papa', 'baba']
# sym = "abco"
# st = "mama oiefr weo baba rwer mama lijoier baba"
# # for w in words:
# #     st = st.replace(w, w.upper())
# # print(st)
#
# word = st.split()
# for s in sym:
#     i = 0
#     while i < len(word):
#         if s in word[i]:
#             word.pop(i)
#             i -= 1
#         i += 1
#
# print(word)

import random

marks = [["Яромил"],["Горигляд"],["Ярополк"],["Цвітан"],["Наслав"],["Іларіон"],["Йозеф"],["Худан"],["Щастибог"]]
for l in marks:
    l.extend([random.randint(6, 12) for i in range(random.randint(4, 10))])

for st in marks:

    for s in st:
        print(s, end=' ')
    print()

maxMarks = 0
list_avg = []
for i in range(len(marks)):
    s = sum(marks[i][1:]) / len(marks[i][1:])
    list_avg.append(s)
    if s > maxMarks:
        maxMarks = s
        stI = i
# print(marks[stI][0])
# print(list_avg)
# print(list_avg)
# for i in range(len(list_avg) - 1):
#     for j in range(len(list_avg) - 1 - i):
#         if list_avg[j] < list_avg[j + 1]:
#             list_avg[j], list_avg[j + 1] = list_avg[j + 1], list_avg[j]
#             marks[j], marks[j + 1] = marks[j + 1], marks[j]
#
# print(list_avg)
# for st in marks:
#     for s in st:
#         print(s,end=' ')
#     print()

for st in marks:
    for i in range(len(st) - 1):
        for j in range(1, len(st) - 1 - i):
            if st[j] < st[j + 1]:
                st[j], st[j + 1] = st[j + 1], st[j]

print()
# for i in range(len(list_avg) - 1):
#     for j in range(len(list_avg) - 1 - i):
#         if list_avg[j] < list_avg[j + 1]:
#             list_avg[j], list_avg[j + 1] = list_avg[j + 1], list_avg[j]
#             marks[j], marks[j + 1] = marks[j + 1], marks[j]

count = [len(el)-1 for el in marks]
# print(count)
for k in range(len(count) - 1):
    for j in range(len(count) - 1 - k):
        if count[j] < count[j+1]:
            count[j], count[j+1] = count[j+1], count[j]
            marks[j], marks[j+1] = marks[j+1], marks[j]

for i in marks:
    for j in i:
        print(j, end=" ")
    print()