def solve(s: str) -> str:
    
    return ''.join(sorted(s))

if __name__ == "__main__":
    for t in range(int(input())):
        s = input().strip()
        print(solve(s))