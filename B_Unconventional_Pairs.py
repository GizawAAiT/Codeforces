def solve(n: int, nums: list[int]) -> int:
    nums.sort()
    
    _min_diff = 0
    for idx in range(0, n, 2):
        _min_diff = max(_min_diff, nums[idx+1]-nums[idx])
    
    return _min_diff

for t in range(int(input())):
    n = int(input())
    nums = [int(_) for _ in input().split()]
    
    print(solve(n, nums))