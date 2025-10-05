from math import isqrt

def solve(nums):
    total = sum(nums)
    
    _square_root = isqrt(total)
    
    if _square_root * _square_root == total:
        return 'YES'
    
    return 'NO'

for t in range(int(input())):
    n = int(input())
    nums = [int(_) for _ in input().split()]
    print(solve(nums))