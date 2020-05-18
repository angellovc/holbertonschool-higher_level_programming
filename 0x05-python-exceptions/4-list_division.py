#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    count = 0
    new = []
    dividend = my_list_1
    divisor = my_list_2
    while count < list_length:
        try:
            new.append(dividend[count]/divisor[count])
        except ZeroDivisionError:
            print("division by 0")
            new.append(0)
        except TypeError:
            print("wrong type")
            new.append(0)
        except IndexError:
            print("out of range")
            new.append(0)
        finally:
            count += 1
    return new
