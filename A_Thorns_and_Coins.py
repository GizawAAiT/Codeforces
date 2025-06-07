def solve(path, n):
    res = 0
    for idx in range(n):
        res += path[idx] =="@"

        if idx > 1 and path[idx] =="*" and path[idx-1]=="*": return res
    
    return res

for _ in range(int(input())):
    n = int(input())
    path = input().strip()
    print(solve(path, n))