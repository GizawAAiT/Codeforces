def _xor(a: str, b: str):
    
    res = ''
    for ai, bi in zip(a, b):
        if ai == bi:
            res += '0'
        else: res += '1'
    
    return res

if __name__ == "__main__":
    a = input().strip()
    b = input().strip()
    
    print(_xor(a, b))