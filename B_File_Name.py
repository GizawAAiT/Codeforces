def solve(name: str):
    running = count = 0
    for char in name:
        if char == 'x':
            running += 1
        
        else:
            running = 0
        
        count += running > 2
    
    return count

n = int(input())
print(solve(
    name = input().strip()
))