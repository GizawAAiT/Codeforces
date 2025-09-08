from collections import Counter

def solve(nums):
    cnt = Counter(nums)
    for k in cnt:
        if cnt[k] == 1:
            return k

for t in range(int(input())):
    nums = [int(_) for _ in input().split()]
    print(solve(nums))