from math import log10
def solve(m: int) -> int:
    
    rounded_down_price = 10 ** int(log10(m))
    
    return m - rounded_down_price

for t in range(int(input())):
    m = int(input())
    print(solve(m))