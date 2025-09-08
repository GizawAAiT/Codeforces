def solve(a, b, c):
    if a < b < c:
        return 'STAIR'
    
    if a < b and c < b:
        return 'PEAK'
    
    return 'NONE'

for t in range(int(input())):
    A, B, C = (int(_) for _ in input().split())
    print(solve(A, B, C))