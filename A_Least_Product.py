from math import prod

def min_operations_to_obtain_least_product(n: int, a: list[int]) -> int:
    _prod = prod(a)
    if _prod <= 0:
        return 0
    
    return 1, 0

for t in range(int(input())):
    n = int(input())
    a = [int(_) for _ in input().split()]
    sol = min_operations_to_obtain_least_product(n, a)
    if sol == 0:
        print(0)
    
    else:
        print(1)
        print(*sol)