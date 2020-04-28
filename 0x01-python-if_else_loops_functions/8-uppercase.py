#!/usr/bin/python3


def uppercase(str):
    """ conver a string lower characters into a upper """
    for letter in str:
        if ord(letter) >= 97 and ord(letter) <= 122:
            letter = chr(ord(letter) - 32)
        print(letter, end='')
    print('')
