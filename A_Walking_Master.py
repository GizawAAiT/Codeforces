# from math import *

def solve(x1, y1, x2, y2):
    if y2 < y1 or (x2-x1)> (y2-y1): return -1
    
    return abs(x2 - (y2-y1)-x1) + (y2-y1)

for _ in range(int(input())):
    x1, y1, x2, y2 = (int(__) for __ in input().strip().split())
    print(solve(x1, y1, x2, y2))