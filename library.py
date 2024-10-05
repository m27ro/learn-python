# import jdatetime
# alan = jdatetime.date.today()
# tavalod = jdatetime.date(1369, 4, 30)
# sen = alan - tavalod
# print(sen / 365)


from math import sqrt
num = [4, 1, 2, 19, 100]
for i in num:
    j = sqrt(i)
    i += 1
    print(f"{j:.4f}")