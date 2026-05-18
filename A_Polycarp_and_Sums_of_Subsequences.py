def solve(nums: list[int]) -> list[int]:
    
    a, b, _max = nums[0], nums[1], nums[-1]
    
    return [a, b, _max - a - b]

for _ in range(int(input())):
    nums = list(map(int, input().strip().split()))
    print(*solve(nums))