def nearest_interesting_number(a: int) -> int:
    
    while digits_sum(a) % 4 != 0:
        a += 1
    
    return a

def digits_sum(n: int) -> int:
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    
    return s

if __name__ == "__main__":
    a = int(input())
    print(nearest_interesting_number(a))