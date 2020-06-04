#!/usr/bin/python3
""" Pascal triangle module """


def pascal_triangle(n):
    """ Return a pascal triangle list """
    triangle = []
    scale = []
    for y in range(0, n):
        scale = []
        for x in range(0, y + 1):
            if x is 0 or x is y:
                scale.append(1)
            else:
                scale.append(triangle[y - 1][x - 1] + triangle[y - 1][x])
        triangle.append(scale)
    return triangle
