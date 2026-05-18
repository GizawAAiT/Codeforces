def solve(n: int, candies: list[int]) -> bool:
    """
    Yes/ No
    """
    if len(candies) < 2: candies.append(0)
    
    # if diff : between max and 2nd max > 1, then NO. Otherwise, YES.
    
    candies.sort()
    
    return candies[-1] - candies[-2] <= 1

for _ in range(int(input())):
    n = int(input())
    candies = list(map(int, input().split()))
    
    print("YES" if solve(n, candies) else "NO")