#!/usr/bin/python3
""" Matrix_divided functions module """


def matrix_divided(matrix, div):
    """
    Make a division of all the elements into the matrix by a div number
    returns a new result list
    Args:
        matrix: matrix of dividends, just floats or integers are allowed
        div: that's represent the divisor, you cannot use 0, because
        division by zero in imposible

    """

    is_matrix = all(isinstance(element, list) for element in matrix)
    if is_matrix is False:  # check if matrix is really a matrix
        errors("no_matrix_error")

    length = len(matrix[0])  # check the corrent length
    for row in matrix:
        if length != len(row):
            errors("len_error")

    for row in matrix:  # check if the elements into the matrix are numbers
        if len(row) == 0:
            errors("no_number_error")
        for element in row:
            if type(element) not in [int, float]:
                errors("no_number_error")

    if div == 0:
        errors("zero_error")
    if type(div) not in [int, float]:
        errors("div_not_number")

    new_matrix = []

    def division(dividend): return round((dividend / div), 2)

    for i in range(0, len(matrix)):  # make the matrix division
        new_matrix.append(list(map(division, matrix[i])))
    return new_matrix


def errors(error):  # errors list
    if error == "len_error":
        raise TypeError("Each row of the matrix must have the same size")
    if error in ["no_number_error", "no_matrix_error"]:
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    if error == "zero_error":
        raise ZeroDivisionError("division by zero")
    if error == "div_not_number":
        raise TypeError("div must be a number")