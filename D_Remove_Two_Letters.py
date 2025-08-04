# def count_distinct_bruteforce(s: str) -> int:
#     n = len(s)
#     seen = set()
#     for i in range(n - 1):
#         t = s[:i] + s[i+2:]          # build in O(n)
#         seen.add(t)
#     return len(seen)
def count_distinct_fast(sequence):
    if len(sequence) < 2:
        return 0

    n = len(sequence)
    base = 256
    mod = 10**9 + 7

    hashes = set()
    prefix_hash = [0] * (n + 1)
    pow_base = [1] * (n + 1)

    # Precompute prefix hashes and base powers
    for i in range(n):
        prefix_hash[i + 1] = (prefix_hash[i] * base 
            + ord(sequence[i])) % mod
        pow_base[i + 1] = (pow_base[i] * base) % mod

    for i in range(n - 1):
        # Hash of substring excluding characters at i and i+1
        left_hash = prefix_hash[i]
        right_hash = (prefix_hash[n] - prefix_hash[i + 2] 
            * pow_base[n - (i + 2)]) % mod
        combined_hash = (left_hash * pow_base[n - (i + 2)] 
            + right_hash) % mod
        hashes.add(combined_hash)
    return len(hashes)
for _ in range(int(input())):
    n = int(input())
    print(count_distinct_fast(sequence=input().strip()))