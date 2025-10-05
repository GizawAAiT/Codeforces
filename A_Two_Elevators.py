def solve(a, b, c):
    dist_a = abs(a-1)
    dist_b = abs(c-b) + abs(c-1)
    if dist_a < dist_b:
        return 1
    
    elif dist_b < dist_a:
        return 2
    
    return 3

for t in range(int(input())):
    a, b, c = (int(_) for _ in input().split())
    print(solve(a, b, c))