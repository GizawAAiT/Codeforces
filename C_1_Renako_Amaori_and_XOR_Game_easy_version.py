def solve(a: list[int], b: list[int]) -> str:
    odd_diff = even_diff = 0
    for idx in range(len(a)):
        ai, bi = a[idx], b[idx]
        if ai != bi:
            odd_diff += idx % 2
            even_diff += (idx + 1) % 2
    
    if even_diff > odd_diff:
        return "Ajisai"
    
    if odd_diff > even_diff:
        return "Mai"
    
    return "Tie"

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve(a, b))