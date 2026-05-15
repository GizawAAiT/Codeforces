from collections import Counter

def solve(arr: list[int]) -> int:
    
    _dic = Counter(arr)
    
    res = 0
    for key, val in _dic.items():
        res += val//2
    
    return res

for _ in range(int(input())):
    _ = int(input())
    arr = list(map(int, input().strip().split()))
    print(solve(arr))