#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    count = 0
    for element in my_list:
        try:
            if count >= x:
                raise Exception("finish")
        except Exception:
            print("")
            return count
        else:
            count += 1
            print("{}".format(element), end="")
    print("")
    return count
