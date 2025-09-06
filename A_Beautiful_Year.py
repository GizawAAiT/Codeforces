def solve(year):
    year += 1
    
    while len(str(year)) != len(set(str(year))):
        year += 1
        
    return year

year = int(input())
print(solve(year))