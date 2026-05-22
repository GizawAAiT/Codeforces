def solve(n: int) -> int:
    liked = set()
    num = 1
    while num ** 2 <= n:
        liked.add(num ** 2)
        if num ** 3 <= n:
            liked.add(num ** 3)
        
        num += 1
        
    return len(liked)

for t in range(int(input())):
    n = int(input())
    print(solve(n))