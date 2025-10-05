def solve(n: int, a: list[int]):
    
    a.sort()
    
    if a[0] == a[-1]:
        return -1
    
    b, c = [], []
    for num in a:
        if num == a[-1]:
            c.append(num)
        else:
            b.append(num)
    
    return [b, c]

for t in range(int(input())):
    n = int(input())
    a = [int(_) for _ in input().split()]
    
    res = solve(n, a)
    if res == -1:
        print(-1)
    
    else:
        print(len(res[0]), len(res[1]))
        print(*res[0])
        print(*res[1])
        
    