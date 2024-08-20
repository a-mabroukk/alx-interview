#!/usr/bin/python3
"""method"""


def minOperations(n):
    """Minimum Operations"""
    if n <= 1:
        return 0  # If n is 1 or less, no operations are needed

    # Initialize dp array to store the minimum operations for each number up to n
    dp = [float('inf')] * (n + 1)
    dp[1] = 0  # Base case: 1 'H' requires 0 operations

    # Function to find all factors of a number
    def get_factors(num):
        factors = []
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                factors.append(i)
                if i != num // i:
                    factors.append(num // i)
        return factors

    # Fill the dp array with minimum operations
    for i in range(2, n + 1):
        factors = get_factors(i)
        for factor in factors:
            if factor != i:  # Skip the factor if it is equal to i
                dp[i] = min(dp[i], dp[factor] + (i // factor))

    return dp[n]
