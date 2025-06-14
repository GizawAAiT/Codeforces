def solve(s: str):
    running, total = 0, 0
    
    for ch in s:
        if ch == '.':
            running += 1
            if running >= 3: 
                return 2
            
            total += 1
                        
        else:
            running = 0
    
    return total

for t in range(int(input())):
    n = input()
    s = input().strip()
    print(solve(s))
    
    