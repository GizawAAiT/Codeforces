def solve(skills):
    finalist_total = max(skills[0], skills[1]) + max(skills[2], skills[3])
    skills.sort()
    if skills[2] + skills[3] == finalist_total:
        return 'YES'
    
    return 'NO'

for t in range(int(input())):
    skills = [int(_) for _ in input().split()]
    print(solve(skills))