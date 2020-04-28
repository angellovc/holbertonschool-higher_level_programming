#!/usr/bin/python3


def print_last_digit(number):
    if number < 0:
        lastdigit = -1 * (abs(number) % 10)  # get las digit in negative number
    else:  # last digit integer number
        lastdigit = number % 10
    print("{:d}".format(lastdigit), end='')
