def solve(num):
    return [n for n in range(1, num+1)]

for t in range(int(input())):
    num = int(input())
    print(*solve(num))