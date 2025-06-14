def solve(n: int, nums: list[int]):
    min_diff = float('inf')
    running_max = nums[0]
    for idx in range(1, n):
        min_diff = min(min_diff, nums[idx]-running_max)
        if min_diff < 0: return 0
        
        running_max = max(running_max, nums[idx])
    
    return min_diff//2 + 1

for t in range(int(input())):
    n = int(input())
    print(solve(
        n = n,
        nums = [int(_) for _ in input().strip().split()]
    ))