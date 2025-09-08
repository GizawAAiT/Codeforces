def solve(nums):
    
    _max = max(nums)
    don = 0
    for num in nums:
        don += _max - num
    
    print(don)
    
n = int(input())
nums = [int(_) for _ in input().split()]
solve(nums)