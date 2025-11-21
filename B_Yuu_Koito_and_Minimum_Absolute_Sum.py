def solve(nums: list[int]) -> int:
    first, last = nums[0], nums[-1]
    if first != -1 and last == -1:
        last = first
    
    if last != -1 and first == -1:
        first = last
    
    if first == -1 and last == -1:
        first = last = 0
    
    # assign first and last:
    nums[0], nums[-1] = first, last
    
    return [num if num != -1 else 0 for num in nums]

for t in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    res = solve(nums)
    print(abs(res[-1] - res[0]))
    print(*res)