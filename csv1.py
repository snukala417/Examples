import csv

f = open('b.csv', 'r')

reader =  csv.reader(f)
i =0
for row in reader:
    print row[3]
    i +=1
print "I value:", i

