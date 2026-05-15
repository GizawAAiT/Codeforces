def solve(n: int) -> int:
    
    if n % 7 == 0: return n

    mod_7, mod_10 = n % 7, n % 10
    if mod_7 <= mod_10:
        return n - mod_7
    
    return n + (7-mod_7)

for _ in range(int(input())): # Test cases
    n = int(input())
    print(solve(n))