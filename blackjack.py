# Jacqui Unciano, jdu5sq
# Description this program is designed to  help calculate the value of Blackjack hands.

def card_to_value(card):
    if "T" == card:  # T is so that 10 doesn't mess with the hand length
        return 10
    elif "J" == card:
        return 10
    elif "Q" == card:
        return 10
    elif "K" == card:
        return 10
    elif "A" == card:
        return 1
    else:
        return int(card)

def hard_score(hand):
    count = 0
    for i in range(0, len(hand)):  # i loops from 0 to the character length of the str hand
        card_value = card_to_value(hand[i])
        count += card_value
    return count

def soft_score(hand):
    if "A" in hand:
        return hard_score(hand) + 10  # adding 10 so that the ace is treated like 11 without messing with the length
    else:
        return hard_score(hand)
