def max_string_value(s: str, k: int, a: list[int]):
    value = 0
    for idx, c in enumerate(s):
        
        value += (idx + 1) * a[ord(c)-ord('a')]
    
    base, _max = len(s), max(a)
    
    for idx in range(k):
        value += (idx + 1 + base) * _max
    
    return value

if __name__ == '__main__':
    s = input()
    k = int(input())
    a = [int(_) for _ in input().split()]
    print(max_string_value(s, k, a))