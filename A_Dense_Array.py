def solve(nums, n):
    ops = 0

    for i in range(n-1):
        _min, _max = min(nums[i], nums[i+1]), max(nums[i], nums[i+1])
        
        while _min < _max/2:
            _min *= 2
            ops += 1
    
    return ops

for t in range(int(input())):
    n = int(input())
    nums = [int(__) for __ in input().split()]
    print(solve(nums, n))