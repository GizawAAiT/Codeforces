def solve(nums, n):
    ans = [1, 2]
    diff = abs(nums[0] - nums[1])
    for i in range(2, n+1):
        a, b = nums[i%n], nums[i-1]
        curr_diff = abs(a - b)
        if curr_diff < diff:
            diff = curr_diff
            ans = [(i%n)+1, i]
    
    return ans

n = int(input())
nums = [int(_) for _ in input().split()]
print(*solve(nums, n))