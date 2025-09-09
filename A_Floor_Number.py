def solve(n, x):
    if n < 3:
        return 1
    
    l, r = 0, n
    
    while l<r-1:
        mid = l + (r-l)//2
        if n <= mid*x + 2:
            r = mid
        else:
            l = mid
    
    return l + 2

for t in range(int(input())):
    n, x = (int(_) for _ in input().split())
    print(solve(n, x))