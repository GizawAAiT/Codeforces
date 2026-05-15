def solve(n: int, x: int, states: list[int]) -> int:
    
    l, r = -1,  -1
    for idx in range(n):
        
        if states[idx] == 1:
            
            l = idx if l == -1 else l
            r = idx
    
    if r-l+1 > x:
        return 'NO'
    
    return 'YES'

for _ in range(int(input())):
    n, x = map(int, input().split())
    states =list(map(int, input().split()))
    print(solve(n, x, states))