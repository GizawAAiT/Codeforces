
from math import gcd
from functools import reduce
def solve(nums):
    G = reduce(gcd, nums)

    x = 2
    while True:
        # check if x is prime
        for d in range(2, int(x**0.5) + 1):
            if x % d == 0:
                break
        else:  # x is prime
            if G % x != 0:
                return x
        x += 1
for t in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    print(solve(nums))