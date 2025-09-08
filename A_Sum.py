def solve(nums):
    nums.sort()
    return 'YES' if nums[-1] == nums[0] + nums[1] else 'NO'

for t in range(int(input())):
    nums = [int(_) for _ in input().split()]
    print(solve(nums))