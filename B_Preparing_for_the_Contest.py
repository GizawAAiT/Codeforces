def solve(n: int, k: int) -> list[int]:
    ans = []
    for num in range(1, k+1):
        ans.append(num)
    
    for num in range(n, k, -1):
        ans.append(num)
    
    return ans

if __name__ == "__main__":
    for t in range(int(input())):
        n, k = map(int, input().strip().split())
        
        print(*solve(n, k))