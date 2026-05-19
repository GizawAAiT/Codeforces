def solve(n: int, k: int) -> str:
    """
    n: th year
    k: leaves lifespan
    Determine whether we left with even or odd number of leaves on the nth year.
    Strategy: Count odds starting from n backward (the last k or all if k>n).
    """
    odd_count = k//2 if n%2 == 0 else (k + 1)//2
    return "YES" if odd_count % 2 == 0 else "NO"

if __name__ == "__main__":
    for _ in range(int(input())):
        n, k = map(int, input().split())
        print(solve(n, k))