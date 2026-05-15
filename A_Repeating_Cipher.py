def decipher(t: str) -> str:
    
    s = ''
    
    repeat, idx = 1, 0
    
    while idx < len(t):
        s += t[idx]
        idx += repeat
        repeat += 1
    
    return s

if __name__ == '__main__':
    n = int(input())
    t = input().strip()
    print(decipher(t))