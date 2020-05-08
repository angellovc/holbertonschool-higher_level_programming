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
    for digit in roman_string:  # translate roman to decimal
        decimal.append(Roman[digit])
    decimal.append(0)
    for position in range(1, len(decimal)):
        # add numbers if the right number is bigger than actual
        if decimal[position - 1] < decimal[position]:
            result -= decimal[position - 1]
        else:
            result += decimal[position - 1]
    return result
