def time_to_take_machine_a_number_to_zero(
    n: int, q: int, s: str, a: list[int]) -> int:
    
    if 'B' not in s: return a
    
    res = []
    for num in a:
        seconds, idx = 0, 0
        while num > 0:
            if s[idx] == 'A':
                num -= 1
            else: 
                num //= 2
            
            seconds += 1
            
            idx = (idx + 1) % n
            
        res.append(seconds)
    
    return res

if __name__ == '__main__':
    for t in range(int(input())):
        n, q = map(int, input().split())
        s = input()
        a = [int(_) for _ in input().split()]
        res = time_to_take_machine_a_number_to_zero(n, q, s, a)
        
        for r in res:
            print(r)        