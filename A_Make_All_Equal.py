from collections import Counter

def solve(nums, n):
    cnt = Counter(nums)
    return n - max(cnt.values())

for _ in range(int(input())):
    n = int(input())
    nums = [int(_) for _ in input().split()]
    print(solve(nums, n))

