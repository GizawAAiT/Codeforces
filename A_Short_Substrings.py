def solve(b):
    a = ''
    for idx in range(len(b)):
        if idx == 0 or idx%2:
            a += b[idx]
    
    return a

for t in range(int(input())):
    b = input().strip()
    print(solve(b))