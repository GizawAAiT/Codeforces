def min_number_of_operation(n: int, s: str) -> int:
    changes = 0
    for idx in range(1, n):
        changes += s[idx] != s[idx-1]
    
    if changes == 0: return 0
    
    return changes if s[0] == '1' else changes - 1

if __name__ == "__main__":
    for t in range(int(input())):
        n = int(input())
        s = input()
        print(min_number_of_operation(n, s))