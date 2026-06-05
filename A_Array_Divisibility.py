def find_divisible_array_for_all_k(n: int) -> list[int]:
    return [i+1 for i in range(n)]

for t in range(int(input())):
    n = int(input())
    print(*find_divisible_array_for_all_k(n))