def solve(s: str, bounds: list[tuple]) -> int:
    cum_sum = [0]
    for char in s:
        # :Add diff of char relative to 'a' plus 1 to cum_sum [-1]
        cum_sum.append(cum_sum[-1] + (ord(char) - ord('a') + 1))
        
    return [cum_sum[r] - cum_sum[l-1] for l, r in bounds]

n, q = map(int, input().split())
s = input()
bounds = []
for _ in range(q):
    l, r = map(int, input().split())
    bounds.append((l, r))
    
sol = solve(s, bounds)
for val in sol:
    print(val)