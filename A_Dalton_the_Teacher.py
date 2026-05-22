def solve(n: int, p: list[int]) -> int:
    # count the indices containing same value to the index
    unhappies = sum(v == idx + 1 for idx, v in enumerate(p))
    
    return (unhappies+1)//2

if __name__ == "__main__":
    for t in range(int(input())):
        n = int(input())
        unhappies = [int(_) for _ in input().split()]
        
        print(solve(n, unhappies))