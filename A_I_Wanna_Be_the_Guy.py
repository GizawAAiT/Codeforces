def solve(n, x, y):
    cnt = set()
    for i in range(1, len(x)):
        cnt.add(x[i])
    
    for i in range(1, len(y)):
        cnt.add(y[i])
    
    return 'I become the guy.' if len(cnt) == n else 'Oh, my keyboard!'

n = int(input())
x = [int(_) for _ in input().split()]
y = [int(_) for _ in input().split()]

print(solve(n, x, y))
    