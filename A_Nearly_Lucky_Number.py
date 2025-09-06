def solve(num: str):
    lucky = {'4', '7'}
    
    _count = 0
    for digit in num:
        if digit in lucky:
            _count += 1
        
    return "YES" if _count in (4,7) else "NO"

num = input()
print(solve(num))