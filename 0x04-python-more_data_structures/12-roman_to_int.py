#!/usr/bin/python3


def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    result = 0
    numbers = list()
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
    decimal.append(0)
    decimal.append(0)
    for i in range(1, len(decimal)):
        if decimal[i - 1] < decimal[i]:
            result -= decimal[i - 1]
        else:
            result += decimal[i - 1]
    return result
