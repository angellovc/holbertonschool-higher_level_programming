#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    """ make the sum of tuple elements
    use zip to group all the interative elements in the same index
    into a tuple, map to sum it and tuple to convert the return into a tuple
    """
    tuple_a += (0, 0)  # add 0 to fill void tuples
    tuple_b += (0, 0)
    return tuple(map(sum, zip(tuple_a[0:2], tuple_b[0:2])))
