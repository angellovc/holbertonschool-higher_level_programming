#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """ print a matrix """
    for i in range(len(matrix)):
        for i, number in zip(range(len(matrix[i])), matrix[i]):
            if i == len(matrix[i]) - 1:
                print("{:d}".format(number), end="")
            else:
                print("{:d}".format(number), end=" ")
        print("")
