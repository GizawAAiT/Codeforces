def solve(n: int) -> int:
    mod = n%4
    
    if mod in [1,2]:
        return 1
    
    return 0

n = int(input())
print(solve(n))