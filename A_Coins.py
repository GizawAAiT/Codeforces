def coins_slow(n: int, S: int) -> int:
    """O(S) in the worst case."""
    if n == 0 or S == 0:
        return 0
    cnt = 0
    while S >= n:        # repeatedly use a coin of value n
        S -= n
        cnt += 1
    if S > 0:            # leftover 1 … n-1   ⇒ one more coin
        cnt += 1
    return cnt


n, s = (int(_) for _ in input().split())
print(coins_slow(n, s))