#!/usr/bin/python3
"""In a text file, theres is a single character H. Text editor can execute only
two operations in this file: Copy All and paste. Given a number n write a
method that calculate the fewest number operations need to result in exactly n.
"""


def minOperations(n):
    """A function that calcuate fewest no of operation needed in n"""
    total = 0
    operations = 2

    while n > 1:
        while not n % operations:
            total += operations
            n /= operations
        operations += 1
    return total
