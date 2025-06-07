def solve(n, nums):
    nums.sort()
    res = 0
    for idx in range(1, n):
        res += nums[idx]-nums[idx-1]
    
    return res

for _ in range(int(input())):
    n = int(input())
    nums = [int(_) for _ in input().split()]
    print(solve(n, nums))