def solve(s):
    for idx in range(len(s)-1):
        if s[idx] == s[idx+1]:
            return 1
    
    return len(s)

if __name__ == '__main__':
    for t in range(int(input())):
        s = input().strip()
        print(solve(s))