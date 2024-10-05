f = open('./test.txt', 'r')
f.readline()
counter = 0
lines = f.readlines()
for line in lines:
    print(line.strip())
# for line in f:
#     counter += 1
#     this_number = float(line.strip())
#     sum += this_number
#     #print(line.strip())
#     print(sum/counter)