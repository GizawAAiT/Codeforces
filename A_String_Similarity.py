def solve(n: int, binary_str: str) -> str:
    ans = ''
    for idx in range(n):
        ans += binary_str[2 * idx]
    
    return ans

for t in range(int(input())):
    n = int(input())
    binary_str = input()
    print(solve(n, binary_str))