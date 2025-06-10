# n = 5
# for k in range(3):
#     for i in range(n+k-2):
#         for j in range(n+1-i-k):
#             print("  ", end='')
#         for j in range(2*i+1+2*k):
#             if (j == 0 or j == 2*i+2*k) and i == 2+k or (k == 0 and i == 0 and j == 0):
#                 print("# ", end='')
#             else:
#                 print("* ", end='')
#         print()

k = 1
dmax = 31
print("Пн Вт Ср Чт Пт Сб Нд")
for d in range(1-k, dmax+1):
    if d <= 0:
        print("  ", end=' ')
    else:
        print(f"{d:2}", end=' ')
    if (d+k) % 7 == 0:
        print()

print(f"kjflwkejwe {dmax} lwie weio {k}")