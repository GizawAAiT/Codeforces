def solve(n, k):
    # k = max(k, 1)
    
    return (n - 1)*k + 1

for t in range(int(input())):
    n, k = [int(_) for _ in input().split()]
    print(solve(n, k))