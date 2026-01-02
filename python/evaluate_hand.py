import sys
sys.path.append(".")
from python.cards import Deck

def count_ranks(hand):
    counts = {}
    for card in hand:   
        rank = card.rank
        if rank in counts:
            counts[rank] += 1.  #counting how many cards of same rank are in deck
        else:
            counts[rank] = 1
    return counts


"""hand evaluations: most important*
"""

def is_flush(hand):
    suit = hand[0].suit 
    if hand[1].suit == suit and hand[2].suit == suit and hand[3].suit == suit and hand[4].suit == suit:
        return True 
    else:
        return False


def is_straight(hand):
    numbers = []
    for card in hand:
        numbers.append(rank_value(card.rank))
    numbers.sort()
    if numbers[1] == numbers[0] + 1:
        if numbers[2] == numbers[1] + 1:
            if numbers[3] == numbers[2] + 1:
                if numbers[4] == numbers[3] + 1:
                    return True
    else:
        False

def pair(hand):
    counts = count_ranks(hand) 
    for rank in counts:
        if counts[rank] == 2:
            return True
    else:
        return False


def two_pair(hand):
    counts = count_ranks(hand)
    pairs = 0
    for rank in counts:
        if counts[rank] == 2:
            pairs = pairs + 1
    if pairs == 2:
        return True
    else: 
        return False

def three_of_kind(hand):
    counts = count_ranks(hand)
    
    for rank in counts:
        if counts[rank] == 3:
            return True
    return False


def four_of_kind(hand):
    counts = count_ranks(hand)
    
    for rank in counts:
        if counts[rank] == 4: #determining if 4 of the same rank exist 
            return True
    return False


"""def full_house(hand):
    counts = count_ranks(hand)
    has_three = False
    has_two = False
    
    for rank in counts:
        if counts[rank] == 3 and counts[rank] == 2:
        return True
    else:
        return False"""
    


deck = Deck()
hand = [deck.deal(), deck.deal(), deck.deal(), deck.deal(), deck.deal()]

print(f"{hand[0]}, {hand[1]}, {hand[2]}, {hand[3]}, {hand[4]}")

print(f"Flush: {is_flush(hand)}")
print(f"Pair: {pair(hand)}")
print(f"Trips: {three_of_kind(hand)}")