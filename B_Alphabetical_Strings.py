def is_alphabetic_string(s: str) -> bool:
    i, j, curr = 0, len(s)-1, max(s[0], s[-1])
    while i<j:
        if curr == s[i]:
            i += 1
            curr = chr(ord(curr)-1)
        
        elif curr == s[j]:
            j -= 1
            curr = chr(ord(curr) - 1)
        
        else:
            return 'NO'
    
    if curr == 'a' == s[i]: return 'YES'
    return 'NO'

for t in range(int(input())):
    s = input()
    print(is_alphabetic_string(s))