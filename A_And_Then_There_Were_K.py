from math import log
def solve(n: int):
    return 2**int(log(n, 2)) -1

for t in range(int(input())):
    n = int(input())
    print(solve(n))