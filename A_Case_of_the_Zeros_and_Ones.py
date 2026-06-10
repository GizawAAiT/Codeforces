def minimum_length_of_strings_after_removing_consecutive_01s_or_10s(
    n: int, s: str) -> int:
    
    return n - 2 * (min(s.count('1'), s.count('0')))

if __name__ == "__main__":
    n = int(input())
    s = input().strip()
    print(minimum_length_of_strings_after_removing_consecutive_01s_or_10s(
        n, s
    ))