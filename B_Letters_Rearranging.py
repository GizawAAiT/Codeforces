def good_string(s: str) -> str:
    for idx in range(1, len(s)):
        if s[0] != s[idx]:
            return s[:idx] + s[idx:][::-1]
    
    return -1
if __name__ == '__main__':
    for t in range(int(input())):
        s = input()
        print(good_string(s))