#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)  # random number
""" this script check the last digit of a random number """
if number < 0:  # get the las digit in negative numbers
    lastdigit = -1 * (abs(number) % 10)
else:  # get the last digit
    lastdigit = number % 10
if lastdigit >= 6:
    print("Last digit of {:d} is {:d}\
 and is greater than 5".format(number, lastdigit))
elif lastdigit == 0:
    print("Last digit of {:d} is {:d}\
 and is zero".format(number, lastdigit))
elif lastdigit <= 5:
    print("Last digit of {:d} is {:d}\
 and is less than 6 and not 0".format(number, lastdigit))
