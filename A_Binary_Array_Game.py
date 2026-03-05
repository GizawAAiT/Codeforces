def solve(nums):
    if 1 in [nums[0], nums[-1]]:
        return "Alice"
    
    if sum(nums) == len(nums):
        return "Alice"
    
    return "Bob"

for t in range(int(input())):
    n = int(input())
    nums = [int(x) for x in input().strip().split()]
    print(solve(nums))