from math import log, ceil, floor
def solve(x: int):
    if x == 1: return 1 #fucking basecase
    
    magic_list = [0, 1,3,6,10]
    digit = x%10
    res = (digit - 1)*10
    return res + magic_list[ceil(log(x, 10))]

for t in range(int(input())):
    x = int(input())
    
    print(solve(x))