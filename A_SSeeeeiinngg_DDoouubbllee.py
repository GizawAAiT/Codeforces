def doubled_string_palindrome(s: str) -> str:
    return s + s[::-1]

if __name__ == "__main__":
    for t in range(int(input())):
        s = input()
        print(doubled_string_palindrome(s))