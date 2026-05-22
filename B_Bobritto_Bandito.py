def solve(n: int, m: int, l: int, r: int) -> tuple[int, int]:
    l_prime = max(-m, l)
    r_prime = l_prime + m
    
    return (l_prime, r_prime)

for t in range(int(input())):
    n, m, l, r = map(int, input().split())
    print(*solve(n, m, l, r))