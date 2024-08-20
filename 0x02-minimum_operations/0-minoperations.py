#!/usr/bin/python3
"""method"""


def minOperations(n):
    """Minimum Operations"""
    dp = [float('inf')] * (n + 1)
    if dp[i] < 1:
        return 0
    dp[1] = 1

    for i in range(2, n + 1):
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        dp[i] = min(dp[i], dp[i - 1] + 1)
