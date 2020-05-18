#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    digits_printed = 0
    while count < x:
        try:
            print("{:d}".format(my_list[count]), end="")
            count += 1
            digits_printed += 1
        except (ValueError, TypeError):
            count += 1
            continue
    print("")
    return digits_printed
