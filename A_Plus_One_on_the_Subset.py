def solve(nums):
    return max(nums) - min(nums)

for t in range(int(input())):
    n = int(input())
    nums = [int(_) for _ in input().split()]
    print(solve(nums))