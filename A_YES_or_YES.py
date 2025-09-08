def solve(inp, pattern = 'yes'):
    if inp.lower() == pattern:
        return 'YES'
    
    return 'NO'

for t in range(int(input())):
    inp = input().strip()
    print(solve(inp))