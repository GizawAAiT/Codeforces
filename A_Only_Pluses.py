def solve(nums):
    for _ in range(5):
        nums.sort()
        nums[0] += 1
    
    return nums[0] * nums[1] * nums[2]

for _ in  range(int(input())):
    nums = [int(_) for _ in input().split()]
    print(solve(nums))