# def solve(nums, n):
#     total = sum(nums)
#     if total % n: return -1

#     av = total//n
#     return sum([num>av for num in nums])
"""
Find minimum number of contributor departments needed for equal redistribution.
"""
from typing import Dict, List
from itertools import combinations

def find_minimum_contributors(amounts) -> int:
    # amounts = list(donations.values())
    total = sum(amounts)
    n = len(amounts)

    if total % n != 0:
        return -1  # Redistribution impossible if total isn't divisible equally.

    average = total // n
    contributors = sum(amount > average for amount in amounts)

    return contributors

for _ in range(int(input())):
    n = int(input())
    nums = [int(_) for _ in input().split()]
    print(find_minimum_contributors(nums))