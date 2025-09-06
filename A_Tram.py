def solve(trams):
    _capacity = max_capacity = 0
    
    for dropped, entered in trams:
        _capacity -= dropped
        _capacity += entered
        max_capacity = max(max_capacity, _capacity)
    
    return max_capacity

n = int(input())
trams = []        
for _ in range(n):
    t = (int(_) for _ in input().split())
    trams.append(t)

print(solve(trams))