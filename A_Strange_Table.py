def solve(n: int, m: int, x: int) -> int:
    c = (x + n - 1)//n
    r = x % n if x%n != 0 else n
    
    cell = (r-1)*m + c
    
    return cell

for t in range(int(input())):
    n, m, x = map(int, input().split())
    print(solve(n, m, x))