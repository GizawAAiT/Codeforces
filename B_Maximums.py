def restore_array_a(b: list[int]) -> list[int]:
    a = []
    _max = 0
    for num in b:
        _max += num if num > 0 else 0
        a.append(_max if num >= 0 else _max + num)
    
    return a

if __name__ == '__main__':
    n = int(input())
    b = [int(_) for _ in input().split()]
    print(*restore_array_a(b=b))