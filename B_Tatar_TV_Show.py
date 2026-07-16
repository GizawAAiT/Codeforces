def can_obtain_zero_binary_string(n: int, k: int, s: list[int]) -> str:
    
    for idx in range(n-k):
        if s[idx] == 1:
            s[idx] = 0
            s[idx+k] = 1 - s[idx+k]
    
    return 'YES' if sum(s) == 0 else 'NO'

if __name__ == '__main__':
    for t in range(int(input())):
        n, k = map(int, input().split())
        s = [int(_) for _ in input()]
        print(can_obtain_zero_binary_string(n, k, s))