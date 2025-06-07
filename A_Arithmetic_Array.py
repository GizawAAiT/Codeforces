def solve(nums, n):
    total = sum(nums)
    if total < n: return 1

    if total == n: return 0

    return total - n 

for t in range(int(input())):
    n = int(input())
    nums = [int(_) for _ in input().strip().split()]

    print(solve(nums, n))
