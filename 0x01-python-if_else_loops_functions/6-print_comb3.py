#!/usr/bin/python3

for tens in range (0, 10):
    for units in range (tens + 1, 10):
        if units == 9 and tens == 8:
            print("{}{}".format(tens, units))
        else:
            print("{}{}, ".format(tens, units), end='')
