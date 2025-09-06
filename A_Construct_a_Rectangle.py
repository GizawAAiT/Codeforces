def solve(lengths: list[int]):
    for idx in range(3):
        l, l1, l2 = lengths[idx], lengths[(idx+1)%3], lengths[(idx+2)%3]
        
        if (l1 == l2 and  l%2 == 0) or (l1+l2 == l):
            return "YES"
        
    return "NO"
    
for t in range(int(input())):
    lengths = [int(_) for _ in input().split()]
    print(solve(lengths))
    