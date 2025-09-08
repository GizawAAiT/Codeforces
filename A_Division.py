def solve(rating):
    if rating >= 1900:
        return 'Division 1'
    
    if 1600 <= rating < 1900:
        return 'Division 2'
    
    if 1400 <= rating < 1600:
        return 'Division 3'
    
    return 'Division 4'

if __name__ == '__main__':
    for t in range(int(input())):
        rating = int(input())
        print(solve(rating))