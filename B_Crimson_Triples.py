def number_of_crimson_triplet(n: int) -> int:
    accumulator = 0
    for b in range(1, n+1):
        accumulator += (n//b) ** 2
    
    return accumulator

for t in range(int(input())):
    n = int(input())
    print(number_of_crimson_triplet(n))