def solve(table_card: str, hand_cards: list[str]):
    for s, l in hand_cards:
        if s in table_card or l in table_card:
            return 'YES'
    
    return 'NO'

table_card = input().strip()
hand_cards = input().split()
print(solve(table_card, hand_cards))