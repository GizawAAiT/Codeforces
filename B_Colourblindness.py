def solve(n, color_a, color_b):
    for idx in range(n):
        if 'R' in (color_a[idx], color_b[idx]) and color_a[idx] != color_b[idx]:
            return 'NO'
    
    return 'YES'

for t in range(int(input())):
    n = int(input())
    color_a = input()
    color_b = input()
    
    print(solve(n, color_a, color_b))