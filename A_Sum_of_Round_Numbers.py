def solve(nums: str):
    n = len(nums)
    res = []
    for idx, num in enumerate(nums):
        if num != '0':
            res.append(num + '0'*(n-1-idx))
    
    return res

for t in range(int(input())):
    nums = input().strip()
    res = solve(nums)
    print(len(res))
    print(*res)