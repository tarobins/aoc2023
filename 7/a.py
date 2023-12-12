from absl import app
import functools

card_values = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

def has_five_of_a_kind(hand):
    cards = dict()
    j_count = 0
    for card in hand:
        if card == 'J':
            j_count += 1
            continue
        if card in cards:
            cards[card] += 1
        else:
            cards[card] = 1
    if 5 in cards.values():
        return True
    if 4 in cards.values() and j_count > 0:
        return True
    if 3 in cards.values() and j_count > 1:
        return True
    if 2 in cards.values() and j_count > 2:
        return True
    if j_count > 3:
        return True
    
def has_four_of_a_kind(hand):
    cards = dict()
    j_count = 0
    for card in hand:
        if card == 'J':
            j_count += 1
            continue
        if card in cards:
            cards[card] += 1
        else:
            cards[card] = 1
    if 4 in cards.values():
        return True
    if 3 in cards.values() and j_count > 0:
        return True
    if 2 in cards.values() and j_count > 1:
        return True
    if j_count > 2:
        return True
    
def has_full_house(hand):
    cards = dict()
    j_count = 0
    for card in hand:
        if card == 'J':
            j_count += 1
            continue
        if card in cards:
            cards[card] += 1
        else:
            cards[card] = 1
    if 3 in cards.values() and 2 in cards.values():
        return True
    if list(cards.values()).count(2) == 2 and j_count > 0:
        return True
    
def has_three_of_a_kind(hand):
    cards = dict()
    j_count = 0
    for card in hand:
        if card == 'J':
            j_count += 1
            continue
        if card in cards:
            cards[card] += 1
        else:
            cards[card] = 1
    if 3 in cards.values():
        return True
    if 2 in cards.values() and j_count > 0:
        return True
    if j_count > 1:
        return True

def has_two_pairs(hand):
    cards = dict()
    j_count = 0
    for card in hand:
        if card == 'J':
            j_count += 1
            continue
        if card in cards:
            cards[card] += 1
        else:
            cards[card] = 1
    if list(cards.values()).count(2) == 2:
        return True
    if 2 in cards.values() and j_count > 0:
        return True
    
def has_one_pair(hand):
    cards = dict()
    j_count = 0
    for card in hand:
        if card == 'J':
            j_count += 1
            continue
        if card in cards:
            cards[card] += 1
        else:
            cards[card] = 1
    if 2 in cards.values():
        return True
    if j_count > 0:
        return True

def card_comparison(card1, card2):
    if card_values.index(card1) < card_values.index(card2):
        return 1
    elif card_values.index(card1) > card_values.index(card2):
        return -1
    else:
        return 0
    
def high_card_hand_comparison(hand1, hand2):
    for i in range(5):
        if card_comparison(hand1[i], hand2[i]) == 1:
            return 1
        elif card_comparison(hand1[i], hand2[i]) == -1:
            return -1
    return 0

comparison_functions = [has_five_of_a_kind, has_four_of_a_kind, has_full_house, has_three_of_a_kind, has_two_pairs, has_one_pair]

def compare_hands(hand1, hand2):
    for function in comparison_functions:
        if function(hand1) and not function(hand2):
            return 1
        elif function(hand2) and not function(hand1):
            return -1
        elif function(hand1) and function(hand2):
            return high_card_hand_comparison(hand1, hand2)
    return high_card_hand_comparison(hand1, hand2)

def line_comparison(line1, line2):
    return compare_hands(line1[0], line2[0])
    

def main(argv):
    # print(compare_hands('32T3K', 'KK677'))
    filename = argv[1]

    with open(filename, 'r') as f:
        lines = f.readlines()
    lines = list(map(lambda x: [x[0], int(x[1])], (map(lambda x: x.strip().split(' '), lines))))

    # print(lines)

    lines = sorted(lines, key=functools.cmp_to_key(line_comparison))

    print(lines)

    total = 0

    for i in range(len(lines)):
        total += lines[i][1] * (i + 1)

    print(total)

if __name__ == '__main__':
    app.run(main)