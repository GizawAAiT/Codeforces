def solve(x, y, n):
    l, h = 0, n
    while l<h-1:
        mid = l+ (h-l)//2
        if mid*x + y <= n:
            l = mid
        
        else: h = mid
    
    answer = l * x + y
    print(answer)
    
for t in range(int(input())):
    x, y, n = (int(_) for _ in input().split())
    solve(x, y, n)