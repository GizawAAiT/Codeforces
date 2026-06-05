def solve(n: int, a: list[int]) -> int:
    
    stack, _max = [], 0
    for num in a:
        while stack and stack[-1] > num:
            _max = max(stack.pop(), _max)
        
        stack.append(num)
    
    return _max

for t in range(int(input())):
    n = int(input())
    a = [int(_) for _ in input().split()]
    print(solve(n, a))