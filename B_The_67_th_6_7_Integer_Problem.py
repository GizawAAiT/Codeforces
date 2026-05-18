def solve(nums: list[int]) -> int:
    
    neg_sum = -sum(nums)
    _max = max(nums)
    
    return neg_sum + 2 * _max

for _ in range(int(input())):
    nums = list(map(int, input().strip().split()))
    print(solve(nums))