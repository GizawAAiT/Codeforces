from collections import defaultdict

def solve(nums, n):
    _map = defaultdict(int)
    for idx in range(1, n+1):
        if _map[nums[-idx]] > 0:
            return n-idx + 1

        _map[nums[-idx]] += 1

    return 0

for _ in range(int(input())):
    n = int(input())
    nums = [int(_) for _ in input().split()]
    print(solve(nums, n))
