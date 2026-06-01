def solve(reviews: str) -> int:
    return reviews.count('1') + reviews.count('3')

for t in range(int(input())):
    n = int(input())
    reviews = input()
    print(solve(reviews=reviews))