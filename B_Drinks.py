def solve(percents:list[float], n: int):
    
    return sum(percents)/n

n = int(input())
percents = [int(_) for _ in input().split()]
print(solve(percents, n))