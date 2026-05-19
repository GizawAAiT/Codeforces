def solve(n: int, x: int, y: int) -> int:
    speed = min(x, y)
    return (n + speed - 1) // speed

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        x, y = map(int, input().strip().split())
        
        print(solve(n, x, y))