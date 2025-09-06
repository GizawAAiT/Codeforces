def solve(str1, str2):
    n = len(str1)
    for idx in range(n):
        if str1[idx].lower() < str2[idx].lower(): return -1
        if str1[idx].lower() > str2[idx].lower(): return 1
        
    return 0

str1 = input().strip()
str2 = input().strip()
print(solve(str1, str2))
