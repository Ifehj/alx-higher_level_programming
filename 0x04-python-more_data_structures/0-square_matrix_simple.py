#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for x in range(len(matrix)):
        new_matrix[x] = list(map(lambda x: x * x, matrix[x]))

    return (new_matrix)
