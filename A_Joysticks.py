def solve(a, b):
    if min(a, b) < 1: return 0
    
    count = 0
    while max(a, b)>1 and min(a, b)>0:
        count += 1
        if a > b:
            a, b = b, a

        a += 1
        b -= 2
        
    return count     
    
a, b = (int(_) for _ in input().split())
print(solve(a, b))