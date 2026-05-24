def solve(n: int, k: int):
    pairs = n + n//2
    if k <= 2*pairs:
        return (k + 1)//2
    
    return min(k - pairs, 3*n - 2)

for t in range(int(input())):
    n, k = map(int, input().split())
    print(solve(n, k))