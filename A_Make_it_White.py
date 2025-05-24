def solve(s):
    start, end= -1, -1
    for idx, char in enumerate(s):
        if char == 'B':
            start = idx if start == -1 else start
            end = idx
    
    return end - start + 1 if start != -1 else 0

for _ in range(int(input())):
    n = int(input())
    s = input()
    print(solve(s))