def solve(a, b, k):
    
    return a*((k+1)//2) - b*((k//2))

for _ in range(int(input())):
    a, b, k = (int(_) for _ in input().split())
    
    print(solve(a, b, k))