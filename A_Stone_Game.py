def solve(n, nums):
    _min, _max, index_min, index_max = nums[0], nums[0], 0, 0
    
    for idx in range(n):
        if nums[idx] < _min:
            _min = nums[idx]
            index_min = idx

        if nums[idx] > _max:
            _max = nums[idx]
            index_max = idx
    
    l, r = min(index_max, index_min), max(index_max, index_min)
    
    return min(r + 1, n - l, l + 1 + (n-r))

for t in range(int(input())):
    n = int(input())
    nums = [int(_) for _ in input().split()]
    print(solve(
        n = n,
        nums = nums
    ))