def solve(n: int, arr: list[int]) -> int:
    
    res = 0
    for x in arr:
        res ^= x
    
    if res != 0 and n % 2 == 0:
        return -1
    
    return res

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(n, arr))