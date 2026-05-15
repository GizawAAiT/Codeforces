def solve(k: int, x: int) -> int:
    
    # find 2^k times x:
    return 2**k * x

for _ in range(int(input())):
    k, x = map(int, input().strip().split())
    print(solve(k, x))