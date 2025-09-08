def solve(problems, k):
    available = 240-k
    
    l, r = 0, available
    while l < r-1:
        mid = l + (r-l)//2
        
        # can he solve #mid number of problems?
        # first_term = 5
        # last_term = 5*mid
        
        time = ((5+5*mid)/2) * mid
        if time <= available:
            l = mid
        else:
            r = mid
    
    return min(l, problems)

problems, k = (int(_) for _ in input().split())
print(solve(problems, k))
        