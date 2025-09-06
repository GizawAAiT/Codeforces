def solve(ps:  list[int], qs:  list[int]):
    even_ps = even_qs = odd_ps = odd_qs = 0
    
    for p in ps:
        even_ps += (p+1)%2
        odd_ps += p%2
        
    for q in qs:
        even_qs += (q+1)%2
        odd_qs += q%2
        
    return even_ps*even_qs + odd_ps*odd_qs

for t in range(int(input())):
    n = int(input())
    ps = [int(_) for _ in input().split()]
    
    m = int(input())
    qs = [int(_) for _ in input().split()]
    
    print(solve(ps, qs))
    