def solve(n: int, book_shelf: list[int]) -> int:
    l = 0
    while book_shelf[l] == 0: l += 1
    
    r = n-1
    while book_shelf[r] == 0: r -= 1
    
    ans = sum(book_shelf[idx] == 0 for idx in range(l, r))
    return ans

if __name__ =="__main__":
    for t in range(int(input())):
        n = int(input())
        book_shelf = [int(_) for _ in input().split()]
        print(solve(n, book_shelf=book_shelf))