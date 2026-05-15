def solve(n: int, s: str) -> str:
    
    s = s.lower()
    
    stack = []
    
    for c in s:
        if not stack or stack[-1] != c:
            stack.append(c)
        
    return 'YES' if ''.join(stack) == 'meow' else 'NO'

for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    print(solve(n, s))