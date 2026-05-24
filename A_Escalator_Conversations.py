def solve(n: int, m: int, k: int, H: int, h: list[int]) -> int:
    _max = m * k
    ans = 0
    for height in h:
        diff = abs(H - height)
        ans += 0 < diff < _max and diff % k == 0
    
    return ans

for t in range(int(input())):
    n, m, k, H = map(int, input().split())
    h = [int(_) for _ in input().split()]
    print(solve(n, m, k, H, h))    