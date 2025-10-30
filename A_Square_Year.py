def solve(year: int):
    
    for r in range(int(year**0.5) + 1):
        if r*r == year:
            return [0, r]
    
    return [-1]

for t in range(int(input())):
    year = int(input())
    print(*solve(year))