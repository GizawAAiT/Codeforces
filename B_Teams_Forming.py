def solve(n: int, a: list[int]) -> int:
    problem_solved = 0
    a.sort()
    for idx in range(0, n, 2):
        problem_solved += a[idx+1] - a[idx]
    
    return problem_solved

n = int(input())
a = [int(_) for _ in input().split()]
print(solve(n, a))