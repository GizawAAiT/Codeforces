def solve(athletes, n):
    athletes.sort()
    
    min_range = float('inf')
    for idx in range(1, n):
        min_range = min(min_range, athletes[idx]-athletes[idx-1])
    
    return min_range

for _ in range(int(input())):
    n = int(input())
    athletes = [int(__) for __ in input().strip().split()]
    
    print(solve(athletes=athletes, n=n))
    