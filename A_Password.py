def solve(n: int, digits: list[int]) -> int:
    
    num_of_available_digits = 10 - n
    
    # pairs is combination of 2 digs from availables:
    num_pairs = num_of_available_digits * (num_of_available_digits - 1) // 2
    
    # 6 arrangements for each pairs:
    return 6 * num_pairs

for _ in range(int(input())):
    n = int(input())
    digits = list(map(int, input().strip().split()))
    print(solve(n, digits))