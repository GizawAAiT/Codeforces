def solve(constraints: list[tuple[int, int]]) -> list[int]:
    
    lower_bound, upper_bound, num_excluded = 0, float('inf'), 0
    for a, x in constraints:
        if a == 1:
            lower_bound = max(lower_bound, x)
            
        if a == 2:
            upper_bound = min(upper_bound, x)
    
    if lower_bound > upper_bound: 
        return 0
    
    for a, x in constraints:
        if a == 3 and (lower_bound <= x <= upper_bound):
            num_excluded += 1
    
    return upper_bound - lower_bound + 1 - num_excluded
    
for _ in range(int(input())):
    n = int(input())
    constraints = []
    for _ in range(n):
        a, x = (int(_) for _ in input().strip().split())
        constraints.append((a, x))
        
    print(solve(constraints))