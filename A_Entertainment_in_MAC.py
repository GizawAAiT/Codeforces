def solve(s: str) -> str:
    rev = s[::-1]
    
    return s if s <= rev else rev + s
    
if __name__ == "__main__":
    for t in range(int(input())):
        n = int(input())
        s = input().strip()
        
        print(solve(s))