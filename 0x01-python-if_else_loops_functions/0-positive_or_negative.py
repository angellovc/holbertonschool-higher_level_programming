#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)  # random number
"""evalue if a random number is positive or negative"""
if number < 0:
    print("{:d} is negative".format(number))
elif number == 0:
    print("{:d} is zero".format(number))
elif number > 0:
    print("{:d} is positive".format(number))
