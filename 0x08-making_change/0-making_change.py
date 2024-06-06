#!/usr/bin/python3
"""
Inteview Question: making change
"""


def makeChange(coins, total):
    """Function to make change"""
    if total <= 0:
        return 0
    else:
        coins.sort(reverse=True)
        change = 0
        for coin in coins:
            while (total >= coin):
                change += 1
                total -= coin

        if total == 0:
            return change
        return -1
