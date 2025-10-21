import random
import datetime

# week = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
# f = open("log.txt", "w")
# for i in range(10000):
#     f.write("192.168.0." + str(random.randint(100, 255)) + " " + week[random.randint(0,6)] + " " +
#             str(random.randint(0, 23)).zfill(2) + "." + str(random.randint(0, 59)).zfill(2) + " " +
#             str(random.randint(0, 23)).zfill(2) + "." + str(random.randint(0, 59)).zfill(2) + "\n")




# f = open("log.txt", "r")
# records = f.read().split('\n')
# ip = [el.split()[1] for el in records]
# # print(records)
# # for rec in records:
# #     ip.append(rec.split()[0])
# uniq_ip = set(ip)
# # uniq_ip = []
# # for rec in ip:
# #     if rec not in uniq_ip:
# #         uniq_ip.append(rec)
# max_count = 0
# for uip in uniq_ip:
#     c = ip.count(uip)
#     if c > max_count:
#         max_count = c
#         max_ip = uip
#
# print(max_count, max_ip)


def totalMinutes(t1: datetime.time, t2: datetime.time) -> int:
    if t2.hour > t1.hour:
        dh = t2.hour - t1.hour
    else:
        dh = 24 - t1.hour + t2.hour
    if t2.minute > t1.minute:
        dm = t2.minute - t1.minute
    else:
        dm = 60 - t1.minute + t2.minute
    return 60 * dh + dm



# f = open("log.txt", "r")
# records = f.read().split('\n')
#
# t2 = datetime.time(int(records[0].split()[2].split('.')[0]), int(records[0].split()[2].split('.')[1]))
# print(t2.hour, t2.minute)


# d1 = datetime.datetime.now()
# d2 = datetime.datetime(2025, 10, 21, 19, 00)
#
# print(d2-d1)
t1 = datetime.time(10, 15)
t2 = datetime.time(15, 33)
print(totalMinutes(t1, t2))
# print(t2)
# tt = t1


def sum(a, b):
    return a + b