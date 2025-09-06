def solve(word):
    n = len(word)
    if n%2: return 'NO'
    
    mid = n//2
    if word[:mid] == word[mid:]:
        return "YES"
    return "NO"

for t in range(int(input())):
    word = input().strip()
    print(solve(word))