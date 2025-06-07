def solve(nums, n):
    total = sum(nums)
    if total % n: return -1

    av = total//n
    return sum([num>av for num in nums])

for _ in range(int(input())):
    n = int(input())
    nums = [int(_) for _ in input().split()]
    print(solve(nums, n))