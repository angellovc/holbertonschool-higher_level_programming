#!/usr/bin/python3


def roman_to_int(roman_string):
    result = 0
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
    for i in range(0, len(decimal)):
        if i < len(decimal) - 1:
            if decimal[i] < decimal[i + 1]:
                result -= decimal[i]
            else:
                result += decimal[i]
    return result
