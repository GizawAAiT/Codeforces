def solve(nums):
    return max(nums) - min(nums)

nums = [int(_) for _ in input().split()]
print(solve(nums))