def have_anyone_lied(n: int, a: list[int]) -> str:
    win_cnt = 0
    for idx in range(1, n):
        if a[idx] == a[idx - 1] == 0:
            return 'YES'
        
        win_cnt += a[idx]
    
    win_cnt += a[0]
    
    return 'NO' if win_cnt < n else 'YES'

if __name__ == "__main__":
    for t in range(int(input())):
        n = int(input())
        a = [int(_) for _ in input().split()]
        print(have_anyone_lied(n, a))