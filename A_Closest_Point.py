def solve(nums):
    if len(nums) == 2 and abs(nums[0] - nums[1]) > 1:
        return 'YES'
    
    return 'NO'

for t in range(int(input())):
    n = int(input())
    nums = [int(_) for _ in input().split()]
    
    print(solve(nums))