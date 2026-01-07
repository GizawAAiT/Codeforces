
def solve(n, m, requirements):
    curr_bit, jump_count = 0, 0
    for minute in range(m):
        if (minute + 1) in requirements.keys() and requirements[minute + 1] == curr_bit:
            continue
        curr_bit += 1 if curr_bit == 0 else -1
        jump_count += 1
    
    return jump_count
        
for t in range(int(input())):
    n, m = (int(_) for _ in input().strip().split())
    requirements = {}
    for _ in range(n):
       minute, bit = (int(x) for x in input().strip().split())
       requirements[minute] = bit
    
    print(solve(n, m, requirements))