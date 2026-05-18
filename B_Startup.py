
def solve(n: int, k: int, bottles: list[tuple[int, int]]) -> int:
    """
    bottles: list of tuples (brand_idx, cost).
    """
    
    # have a list of size k, store total cost of each bottle at that brand idx:
    _costs = [0] * k
    for bi, ci in bottles:
        _costs[bi - 1] += ci
    
    # sort the costs in descending order:
    _costs.sort(reverse=True)
    
    # return the sum of the top n costs:
    return sum(_costs[:n])

for _ in range(int(input())):
    n, k = map(int, input().split())
    bottles = []
    for _ in range(k):
        brand_index, cost = map(int, input().split())
        bottles.append((brand_index, cost))
        
    print(solve(n, k, bottles))