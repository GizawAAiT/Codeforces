def solve(n: int, k: int):
    total = 4*n - 2
    if k == total:
        return 2*n
    
    return (k+1)//2

for t in range(int(input())):
    n, k = map(int, input().split())
    print(solve(n, k))