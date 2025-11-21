def solve(n: int, m: int) -> str:
    
    diff = n - m
    
    if diff < 0 or diff % 2: return "No"
    
    return "Yes"

for t in range(int(input())):
    n, m = map(int, input().split())
    print(solve(n, m))