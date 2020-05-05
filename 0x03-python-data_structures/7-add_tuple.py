#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    """ make the sum of tuple elements
    use zip to group all the interative elements in the same index
    into a tuple, map to sum it and tuple to convert the return into a tuple
    """
    if len(tuple_a) < 1:  # concatenate elements when tuple is void
        tuple_a += (0, 0)
    elif len(tuple_a) < 2:
        tuple_a += (0,)
    if len(tuple_b) < 1:
        tuple_b += (0, 0)
    elif len(tuple_b) < 2:
        tuple_b += (0,)
    if len(tuple_a) > 2:
        tuple_a = tuple_a[0:2]
    return tuple(map(sum, zip(tuple_a, tuple_b)))
