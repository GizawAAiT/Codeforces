def solve(n, nums):
    _max = [0, 0]
    
    for idx, num in enumerate(nums):
        _max[idx%2] = max(num, _max[idx%2])
    
    even_sum = (n+1)//2 + _max[0]
    odd_sum = n//2 + _max[1]
    
    return max(even_sum, odd_sum)

for t in range(int(input())):
    n = int(input())
    nums = [int(_) for _ in input().split()]
    print(solve(n, nums))