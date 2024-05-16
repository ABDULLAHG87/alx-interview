#!/usr/bin/python3
"""Script file for N Queen Placement in NxN cheshboard"""

import sys


def is_safe(q, x, array):
    if x in array:
        return (False)
    else:
        return all(abs(array[column] - x) != q - column
                   for column in range(q))


def place_queen(queen, column, prev_solution):
    safe_position = []
    for array in prev_solution:
        for k in range(column):
            if is_safe(queen, k, array):
                safe_position.append(array + [k])
    return safe_position


def generate_solution(row, column):
    solution = [[]]
    for queen in range(row):
        solution = place_queen(queen, column, solution)
    return solution


def initialize():
    if len(sys.argv) != 2:
        print("Usage: nqueen N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def n_queens():
    n = initialize()
    results = generate_solution(n, n)
    for array in results:
        clean = []
        for q, k in enumerate(array):
            clean.append([q, k])
        print(clean)


if __name__ == '__main__':
    n_queens()
