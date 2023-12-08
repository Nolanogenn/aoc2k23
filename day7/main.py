def typextractor(hand):
    first_card = hand[0]
    unique_cards = set(hand)
    num_unique_cards = len(unique_cards)
    if num_unique_cards == 1:
        return 'fives'
    elif num_unique_cards == 5:
        return 'highcard'
    elif num_unique_cards == 4:
        return 'pair'
    elif num_unique_cards == 3:
        if any([hand.count(x) == 3 for x in unique_cards]):
            return 'tris'
        else:
            return 'twopairs'
    elif num_unique_cards == 2:
        if any([hand.count(x) == 4 for x in unique_cards]):
            return 'poker' 
        else:
            return 'full'
    pass

def parser(inputfile, cards_i, types_i):
    hands_bid = [line.split() for line in inputfile]
    hands = [l[0] for l in hands_bid]
    bids = [l[1] for l in hands_bid]
    hands_played = []
    for i, hand in enumerate(hands):
        t = typextractor(hand)
        h = [cards_i[c] for c in hand]
        hands_played.append(([types_i[t]]+h, bids[i]))
    return hands_played

def part1(inputfile):
    orderedcards = ['A', 'K', 'Q', 'J', 'T', '9', '8','7', '6', '5', '4', '3', '2']
    cards_i = {c:i for i, c in enumerate(orderedcards)}
    ordertypes = ['fives', 'poker', 'full', 'tris', 'twopairs', 'pair', 'highcard']
    types_i = {t:i for i, t in enumerate(ordertypes)}

    hands = parser(inputfile, cards_i, types_i)
    sorted_hands = sorted(hands, key=lambda x:x[0])[::-1]
    won = [(i+1)*int(h[1]) for i,h in enumerate(sorted_hands)]
    return (sum(won))

def typextractor2(hand):
    first_card = hand[0]
    num_j = hand.count('J')
    if num_j == 5:
        return ('fives')
    actual_hand = hand.replace('J', '')
    tmp_hand = actual_hand + 'abcde'[:num_j]
    actual_t = typextractor(tmp_hand)
    if actual_t == 'highcard':
        h2 = actual_hand + (actual_hand[0] * num_j)
        t2 = typextractor(h2)
        return(t2)
    if actual_t in ['pair', 'twopairs']:
        p = [x for x in actual_hand if actual_hand.count(x) == 2][0]
        h2 = actual_hand + (p * num_j)
        t2 = typextractor(h2)
        return(t2)
    if actual_t == 'tris':
        p = [x for x in actual_hand if actual_hand.count(x) == 3][0]
        h2 = actual_hand + (p * num_j)
        t2 = typextractor(h2)
        return(t2)
    if actual_t == 'poker':
        p = [x for x in actual_hand if actual_hand.count(x) == 4][0]
        h2 = actual_hand + (p * num_j)
        t2 = typextractor(h2)
        return(t2)
    return actual_t

                

def parser2(inputfile, cards_i, types_i):
    hands_bid = [line.split() for line in inputfile]
    hands = [l[0] for l in hands_bid]
    bids = [l[1] for l in hands_bid]
    hands_played = []
    for i, hand in enumerate(hands):
        t = typextractor2(hand)
        h = [cards_i[c] for c in hand]
        hands_played.append(([types_i[t]]+h, bids[i]))
    return hands_played

def part2(inputfile):
    orderedcards = ['A', 'K', 'Q', 'T', '9', '8','7', '6', '5', '4', '3', '2', 'J']
    cards_i = {c:i for i, c in enumerate(orderedcards)}
    ordertypes = ['fives', 'poker', 'full', 'tris', 'twopairs', 'pair', 'highcard']
    types_i = {t:i for i, t in enumerate(ordertypes)}
    
    hands = parser2(inputfile, cards_i, types_i)
    sorted_hands = sorted(hands, key=lambda x:x[0])[::-1]
    won = [(i+1)*int(h[1]) for i,h in enumerate(sorted_hands)]
    return (sum(won))

if __name__ == "__main__":
    inputfile = open('./day7test.txt').readlines()
    sol1 = part1(inputfile)
    print(f"Solution for part 1: {sol1}")
    sol2 = part2(inputfile)
    print(f"Solution for part 2: {sol2}")
