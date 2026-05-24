def solve(n: int, m: int, a: str, b: str) ->int:
    k, m_idx = 0, 0
    while k < n and m_idx < m:
        if a[k] == b[m_idx]: 
            k += 1
        m_idx += 1
    
    return k

for t in range(int(input())):
    n, m = map(int, input().split())
    a, b = input(), input()
    print(solve(n, m, a, b))