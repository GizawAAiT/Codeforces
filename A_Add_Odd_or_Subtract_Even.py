def solve(a: int, b: int):
    if a==b: return 0
    
    same_parity = a%2 == b%2
    
    if same_parity:
        return 2 if a<b else 1
    
    else:
        return 1 if a < b else 2
    

for _ in range(int(input())):
    a, b = (int(_) for _ in input().split())
    print(solve(a, b))
    