from collections import defaultdict
from math import ceil

def solve(arr):
    cnt = defaultdict(int)
    for ch in arr:
        cnt[ch] += 1

    changes = max(0, ceil(len(arr)/2) - cnt["1"])
    return changes if (cnt['-1']-changes)%2  == 0 else changes + 1

for _ in range(int(input())):
    input()
    arr = input().strip().split()    
    print(solve(arr))