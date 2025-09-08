def solve(nums):
    nums.sort()
    return "YES" if nums[-1] + nums[-2] >= 10 else 'NO'

for t in range(int(input())):
    nums = [int(_) for _ in input().split()]
    
    print(solve(nums))