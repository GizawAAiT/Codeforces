def solve(k, l, m, n, d):
    _count = 0
    for i in range(1, d+1):
        _count += 0 in [i%k, i%l, i%m, i%n]
    
    return _count

k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

print(solve(k, l, m, n, d))