def solve(n: int) -> int:
    
    left_over = n % 4
    
    if left_over < 2 or n < 4:
        return left_over
    
    if n > 4:
        return left_over % 2
    
    return left_over

for _ in range(int(input())):
    n = int(input())
    print(solve(n))