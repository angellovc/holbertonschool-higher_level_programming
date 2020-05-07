#!/usr/bin/python3


def roman_to_int(roman_string):
    decimal = []
    Roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000}
    for digit in roman_string:
        decimal.append(Roman[digit])
    maxnum = decimal.index(max(decimal))
    n1 = decimal[maxnum:]
    n2 = decimal[0:maxnum]
    number = sum(n1)
    number2 = sum(n2)
    return number - number2
