def solve(words: list[str]):
    res = ''
    for word in words:
        res += word[0]
    
    return res

for t in range(int(input())):
    words = input().split()
    print(solve(words))