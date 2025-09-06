from collections import Counter

def solve(match):
    cnt = Counter(match)
    
    if cnt['A'] > cnt["D"]:
        return 'Anton'
    
    elif cnt['A'] < cnt['D']:
        return 'Danik'
    
    else: return 'Friendship'
    
n = input()
matches = input().strip()
print(solve(matches))