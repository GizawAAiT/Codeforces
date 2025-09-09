def solve(n, pens, notebooks):
    if n <= min(pens, notebooks):
        return 'Yes'
    
    return 'No'

n, pens, notebooks = (int(_) for _ in input().split())
print(solve(n, pens, notebooks))