def solve(problems):
    return len(problems) + len(set(problems))

for t in range(int(input())):
    n = int(input())
    problems = input().strip()
    print(solve(problems))