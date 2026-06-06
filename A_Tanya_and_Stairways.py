def number_of_stairways(n: int, a: list[int]) -> int:
    a.append(0)
    
    stairways_count, steps = 0, []
    for idx in range(1, n+1):
        if a[idx] <= a[idx - 1]:
            stairways_count += 1
            steps.append(a[idx - 1])
    
    return stairways_count, steps

if __name__ == "__main__":
    n = int(input())
    a = [int(_) for _ in input().split()]
    stairways_count, steps = number_of_stairways(n, a)
    print(stairways_count)
    print(*steps)