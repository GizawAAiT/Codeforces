def solve(b: list[int]):
    a = []
    
    a.append(b[0])
    for idx in range(1, len(b)):
        if b[idx] < a[-1]:
            a.append(b[idx])
            
        a.append(b[idx])
    
    # Output:    
    print(len(a))
    print(*a)

for t in range(int(input())):
    n = int(input())
    b = [int(_) for _ in input().split()]
    solve(b)