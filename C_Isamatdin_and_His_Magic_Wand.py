def solve(nums, n):
    # Do i have both parities?
    has_even = any(x % 2 == 0 for x in nums)
    has_odd = any(x % 2 != 0 for x in nums)
    # if both parity, return sorted, else the nums
    if has_even and has_odd:
        return sorted(nums)
    
    return nums

for t in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    result = solve(nums, n-1)
    print(" ".join(map(str, result)))