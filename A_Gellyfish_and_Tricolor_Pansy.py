def winner(a: int, b: int, c: int, d: int) -> str:
    if min(a, c) >= min(b, d):
        return 'Gellyfish'
    
    return 'Flower'

if __name__ == "__main__":
    for t in range(int(input())):
        a, b, c, d = [int(_) for _ in input().split()]
        print(winner(a, b, c, d))