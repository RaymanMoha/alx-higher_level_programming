#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers."""
    for elm in matrix:
        print(" ".join("{:d}".format(i) for i in elm))
