def solve(nums):
    return sorted(nums)

for t in range(int(input())):
    nums = [int(_) for _ in input().split()]
    print(*solve(nums))