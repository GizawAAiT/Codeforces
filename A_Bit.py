def solve(n, ops):
    x = 0
    for op in ops:
        if op[0] == '+' or op[-1] == '+':
            x += 1
        
        else:
            x -= 1
            
    return x

n = int(input())
ops = []
for _ in range(n):
    ops.append(input().strip())

print(solve(n, ops))