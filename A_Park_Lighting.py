def solve(n: int, m: int):
    if n%2 == 0:
        return (n//2) * m
    
    if m %2 == 0:
        return (m//2) * n

    return ((n)//2) * m + ((m+1)//2)

for t in range(int(input())):
    n, m = (int(_) for _ in input().split())
    
    print(solve(
            n = n,
            m = m
            ))