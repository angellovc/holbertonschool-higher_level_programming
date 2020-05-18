#!/usr/bin/python3


def safe_print_division(a, b):
    result = str()
    inside = result
    try:
        result = str(a / b)
        inside = result
        return result
    except ZeroDivisionError:
        inside = None
        return None
    finally:
        print("Inside result: {}".format(inside))