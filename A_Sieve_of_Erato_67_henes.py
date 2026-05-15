def solve(a: list[int]) -> str:
    
    # check if 67 in the list:
    return 'YES' if 67 in a else 'NO'

for _ in range(int(input())):
    _ = input()
    a = list(map(int, input().strip().split()))
    print(solve(a))