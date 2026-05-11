def solve(n: int, arr: list[int]) -> int:
    
    num_1 = num_minus_1 = num_0 = 0
    
    for x in arr:
        if x == 1:
            num_1 += 1
        elif x == -1:
            num_minus_1 += 1
        else:
            num_0 += 1
    
    return num_0 + (num_minus_1 % 2)*2

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(n, arr))