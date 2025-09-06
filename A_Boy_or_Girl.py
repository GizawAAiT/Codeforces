def solve(name):
    if len(set(name)) %2:
        return 'IGNORE HIM!'
    
    return 'CHAT WITH HER!'

name = input()
print(solve(name))