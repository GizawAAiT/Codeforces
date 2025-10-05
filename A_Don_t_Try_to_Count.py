def solve(a, b):

    for num in range(6):
        
        if b in a:
            return num
        
        a += a
    
    return -1

for t in range(int(input())):
    n, m = (int(_) for _ in input().split())
    a = input()
    b = input()
    
    print(solve(a, b))