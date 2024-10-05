from statistics import mean
import csv
with open('test.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        name = row[0]
        last_name = row[1]
        these_test = list()
        for test in row[2:]:
            these_test.append(int(test))
            # print(name, test, these_test)
        print("%s %s average is %f" % (name,last_name, mean(these_test)))