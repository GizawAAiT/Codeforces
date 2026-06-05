def can_color(n: int, arr: list[int]) -> str:
    
    for idx in range(n):
        if idx % 2:
            arr[idx] = (arr[idx], "RED")
        else:
            arr[idx] = (arr[idx], "BLUE")
        
    arr.sort()
    
    for idx in range(1, n):
        if arr[idx][1] == arr[idx - 1][1]:
            return "NO"
    
    return "YES"

for t in range(int(input())):
    n = int(input())
    arr = [int(_) for _ in input().split()]
    print(can_color(n, arr))