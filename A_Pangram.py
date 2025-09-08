def solve(pang):
    characters = set()
    for c in pang:
        characters.add(c.lower())
    
    if len(characters) == 26: return 'YES'
    
    return 'NO'

n = int(input())
pang = input().strip()
print(solve(pang))