def solve(eve):
    polices = untreated = 0
    for e in eve:
        if e < 0:
            untreated += polices < 1
            polices -= polices > 0
        
        else:
            polices += e
    print(untreated)
    
n = int(input())
eve = [int(_) for _ in input().split()]
solve(eve)