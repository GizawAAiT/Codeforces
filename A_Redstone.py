def solve(n: int, a: list[int]) -> str:
    _cnt = {}
    for num in a:
        _cnt[num] = _cnt.get(num, 0) + 1
        if _cnt[num] > 1:
            return 'YES'
    
    return 'NO'

for t in range(int(input())):
    n = int(input())
    a = [int(_) for _ in input().split()]
    print(solve(n, a))