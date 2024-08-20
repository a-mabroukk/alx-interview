#!/usr/bin/python3
"""method"""


def minOperations(n):
    """Minimum Operations"""
    minimumOperations = 2
    totalOperations = 0
    while n > 1:
        while n % minimumOperations == 0:
            totalOperations += minimumOperations
            n /= minimumOperations
        minimumOperations += 1
    return totalOperations
