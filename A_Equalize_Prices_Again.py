def solve(n: int, a: list[int]) -> int:
    """
    Minimum possilbe average price of n goods that gives at least the initial
    total price
    """
    
    total = sum(a)
    return (total + n - 1) // n

for q in range(int(input())):
    n = int(input())
    a = [int(_) for _ in input().split()]
    print(solve(n, a))