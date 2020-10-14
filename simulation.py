import itertools
import random as rd

def my_sort(card):
    return nums.index(card[:-1]) + sym.index(card[-1])/20

def my_print(lst):
    for x in lst:
        print(x,lst[x])

cards_points = {}
cards_links = {}
def comb(tup):
    tmp = list(tup)
    for x in range(2, len(tmp)):
        for k in list(itertools.combinations(tmp, x)):
            if(k[-1][0] == 'A'):
                k = sorted(k, key=my_sort)

            if(not cards_points.get(k)):
                cards_points[k] = (len(tmp) / 12 ) * (1 / 52)**(len(tmp) - x)
                cards_links[k] = tmp

def throw_away_prob(cards):
    # TODO count throw away cards. ex. have [A, 3], 
    # but in TA there are all [2] possible.
    # So probability of [A, 3] can be [A,2,3] = 0

    score = 1
    cards = my_sort(cards)
    if(cards_links.get(cards)):
        s_cards = set(cards)
        s_link = set(cards_links.get(cards))

        diff = s_link.difference(s_cards)

        if(len(diff) > 0):




    else:
        return score



    return 

def generate(n):
    left = 0
    for x in range(len(nums)-n+1):
        for col in sym:
            k = []
            for y in range(x,n+x):
                k.append(nums[y] + col)
            if(k[-1][0] == 'A'):
                k = sorted(k, key=my_sort)
            tupk = tuple(k)
            comb(tupk) 
            cards_points[tupk] = (n / 12) * throw_away_prob(tupk)
            k = []

def generate_ntic():
    for x in nums:
        t = list(map(lambda i: x+i, sym))
        for y in range(2, 5):
            a = list(itertools.combinations(t, y))
            for k in a:
                div = 0
                if(len(k) == 2):
                    div = 1
                    
                cards_points[k] = (len(k)/12)*(1/56)**div
				
def find_duplicate(ar):
    # array must be sorted
    for x in range(len(ar)-1):
        if(ar[x] == ar[x+1]):
            print(ar[x])
            return ar[x]
    return False


def turn(my_deck):
    my_deck = sorted(my_deck, key=my_sort)
    my_sample = []
    for x in my_deck:
        my_sample.append([x,0])

    for a in range(2,13):
	    tmp = list(itertools.combinations(my_deck, a))
	    for x in tmp:
                plus = 0
                if(cards_points.get(x)):
                    plus = cards_points[x]
                    for y in x:
                        for z in my_sample:
                            if(y == z[0]):
                                z[1] += plus

    # Duplicates are not automatically worse, but they are bad.
    duplicate = find_duplicate(my_sample)
    if(duplicate):
        my_deck.remove(duplicate[0])
        return (my_deck, duplicate)

    worst_card = min(my_sample, key=lambda x: x[1])
    played.append(worst_card[0])
    my_deck.remove(worst_card[0])
    return (my_deck, worst_card)


sym = ['♥', '♦', '♠', '♣']
nums = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
my_deck = []

for x in range(2,13):
    generate(x)

generate_ntic()


#all_deck = itertools.product(nums, 2*sym)
all_deck = itertools.product(nums, sym)
deck = list(map(lambda x: x[0]+""+x[1], list(all_deck)))
my_deck = rd.sample(deck, 12)
for x in my_deck:
    deck.remove(x)

played = {}
my_deck = sorted(my_deck, key=my_sort)
while(True):
    smp = rd.sample(list(deck), 1)[0]
    deck.remove(smp)
    my_deck.append(smp)
    t = turn(my_deck)
    my_deck = t[0]
    if(played.get(t[1][0])):
        played[t[1][0]] += 1
    else:
        played[t[1][0]] = 1

    print(f"{my_deck} -> {t[1]}")
    input("continue?")



print(my_deck)
print(played)
print(f"deck sum: {deck_sum}")
