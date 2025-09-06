def solve(a, b):
    years = 0
    while a <= b:
        a *=3
        b *=2
        years += 1
    
    return years
        
a, b = (int(_) for _ in input().split())
print(solve(a, b))