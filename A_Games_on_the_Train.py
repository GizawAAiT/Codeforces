def min_value_of_k(h: list[int]) -> int:
    
    return max(h) - min(h) + 1

if __name__ == "__main__":
    for t in range(int(input())):
        n = int(input())
        h = [int(_) for _ in input().split()]
        print(min_value_of_k(h))