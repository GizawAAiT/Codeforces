def solve(n: int, s: str) -> str:
    for i in range(1, n):
        l, r = s[i-1], s[i]
        
        # If l is Letter and r is digit, return NO
        if not l.isdigit() and r.isdigit():
            return 'NO'
        
        if l > r:
            return 'NO'
        
    return 'YES'

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        s = input().strip()
        print(solve(n, s))