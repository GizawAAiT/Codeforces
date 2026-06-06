def custom_sum(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    for t in range(int(input())):
        a, b = [int(_) for _ in input().split()]
        print(custom_sum(a, b))