# Udacity course
# Auhtor: Harold 
# Init_Date: 18/05/2020
# Last Edit: 18/05/2020
# (see Notion notes for additional information)

def poker(hands):
    "Return the best hand: poker([hand, ...]) => hand"
    return max(hands, key=hand_rank) # or max([rank_hand(hand) for hand in hands])

def hand_rank(hand):
    """Return a value indicating the rank of a hand"""
    ranks = card_rank(hand)
    if straight(ranks) and flush(hand)
        return (8, max(ranks)) # 2 3 4 5 6 -> only thing we need to know is 6 -> (8, 6)
    elif kind(4, ranks)
        # (7, 4 of a a kind rank and then thigh breaker of 1 of a kind (in case multiple decks))
        return (7, kind(4, ranks), kind(1, ranks)) # 9 9 9 9 4 -> (7, 9, 3)
    elif 
    return ???

def test():
    "Test cases for the function in Poker program"
    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()

    # assert means that the following thing must be true
    # if true, moves on, otherwise prints error message
    assert poker([sf, fk, fh]) == sf 
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh

    # Test extremes
    assert poker([sf]) == sf
    assert poker([sf] + [fh for i in range(99)]) # or [sf] + 99*[fh]

    # test rank
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    return "tests pass"

print(test())


