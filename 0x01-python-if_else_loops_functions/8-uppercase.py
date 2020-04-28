#!/usr/bin/python3
""" conver a string lower characters into a upper """


def uppercase(str):
    for letter in str:
        if ord(letter) >= 97 and ord(letter) <= 122:
            letter = chr(ord(letter) - 32)
        print(letter, end='')
    print('')
