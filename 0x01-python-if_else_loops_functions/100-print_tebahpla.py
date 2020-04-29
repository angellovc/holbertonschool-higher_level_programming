#!/usr/bin/python3


""" print the ascii alphabet in reverse using upper and lower characters"""
for lower, upper in zip(range(122, 96, -2), range(89, 64, -2)):
    print("{}{}".format(chr(lower), chr(upper)), end='')  # print ascii numbers
