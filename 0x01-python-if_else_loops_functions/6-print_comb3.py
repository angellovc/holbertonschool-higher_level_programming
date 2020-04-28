#!/usr/bin/python3
count = 0
collector = 2
while (count < 100):
    if count < 89:
        print("{:0>2}, ".format(count), end='')
    else:
        print("{:0>2}".format(count))
    if count % 10 == 9:
        count = count + collector
        collector = collector + 1
    count = count + 1
