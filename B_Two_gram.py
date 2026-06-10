def most_frequent_two_gram_character_wise(n: int, s: str) -> int:
    cnt, most_frequent = {}, s[0] + s[1]
    for idx in range(n-1):
        key = s[idx] + s[idx+1]
        cnt[key] = cnt.get(key, 0) + 1
        if cnt[most_frequent] < cnt[key]:
            most_frequent = key
        
    return most_frequent

if __name__ == '__main__':
    n = int(input())
    s = input().strip()
    print(most_frequent_two_gram_character_wise(n, s))