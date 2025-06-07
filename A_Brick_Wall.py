def solve(n, m):
    # print(n, m)
    # print(m//2, "//", n, n*(m//2))
    return n * (m//2)

for _ in range(int(input())): # Test cases
    n, m = (int(__) for __ in input().split())

    print(solve(n, m))