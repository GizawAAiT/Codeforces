def solve(n: int, m: int, words: list[str]) -> int:
    
    ans = 0
    running_sum_word_length = 0
    for idx, word in enumerate(words):
        running_sum_word_length += len(word)
        
        if running_sum_word_length <= m:
            ans = idx + 1
        else:
            break
    
    return ans

for _ in range(int(input())):
    n, m = map(int, input().strip().split())
    words = []
    for _ in range(n):
        words.append(input().strip())
    print(solve(n, m, words))