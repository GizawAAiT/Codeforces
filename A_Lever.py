def solve(arr: list[int], brr: list[int]) -> int:
    
    num_of_decrement = 0
    for a, b in zip(arr, brr):
        num_of_decrement += max(0, a-b)
    
    return num_of_decrement + 1

for _ in range(int(input())):
    n = int(input())
    arr = [int(_x) for _x in input().split()]
    brr = [int(_x) for _x in input().split()]
    print(solve(arr, brr))