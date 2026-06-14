def k_last_element_sum(n: int, a: list[int]) -> list[int]:
    
    res = []
    _max = 0
    for num in a:
        _max = max(_max, num)
        res.append(_max)
    
    # print(res)
    cum = 0
    for idx in range(n-1, -1, -1):
        res[idx] += cum
        cum += a[idx]
    
    return res[::-1]

if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        a = [int(_) for _ in input().split()]
        print(*k_last_element_sum(n, a))