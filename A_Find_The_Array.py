def solve(s: int) -> int:
    length = 1
    s -= 1
    curr = 1
    
    while s:
        curr += 2
        s -= min(curr, s)
        length += 1
        
    return length

for t in range(int(input())):
    s = int(input())
    print(solve(s))