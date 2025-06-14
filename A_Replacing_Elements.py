def solve(nums, d):
    nums.sort()
    if nums[-1] <= d or nums[0]+nums[1] <= d: return "YES"
    
    return "NO"

for t in range(int(input())):
    n, d = (int(_) for _ in input().split())
    nums = [int(_) for _ in input().split()]
    
    print(solve(nums, d))
    