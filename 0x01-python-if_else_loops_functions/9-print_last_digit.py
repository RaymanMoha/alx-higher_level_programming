#!/usr/bin/python3

def print_last_digit(number):
    """Function that prints the last digit of a number"""
    """Returns the value of the last digit"""
    print(abs(number) % 10, end='')
    return (abs(number) % 10)
