import itertools
import random as rd
def my_sort(card):
    return nums.index(card[:-1]) + sym.index(card[-1])/20

def my_print(lst):
    for x in lst:
        print(x,lst[x])
cards_points = {}
def comb(tup):
    tmp = list(tup)
    for x in range(2, len(tmp)):
        for k in list(itertools.combinations(tmp, x)):
            if(k[-1][0] == 'A'):
                k = sorted(k, key=my_sort)
            if(not cards_points.get(k)):

                cards_points[k] = (len(tmp)/12)*(1/52)**(len(tmp)-x)

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
            cards_points[tupk] = (n / 12)
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
				
#def throw():
#def add():
#def stats():
#def...

def find_duplicates(ar):
    # array is sorted
    for x in range(len(ar)-1):
        if(ar[x] == ar[x+1]):
            ar.remove(ar[x])
    return ar

def parse_input(cmd):
	if(cmd == "stats"):
		stats()
	else:
		print("Unknown command")
	# commands ->
	# throw: print card which is least usefull, automatically adding card to throw stack
	# stack $card: Adding card do stack of used card, automatically removing from possible cards.
	# stats: print statistics of my card and other usefull info(min number of card required to win, mean, max)
	# (optional) oponent show $name_of_oponent $cards(comma separated)
	return 0

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


	worst_card = min(my_sample, key=lambda x: x[1])
	played.append(worst_card[0])
	my_deck.remove(worst_card[0])
	return (my_deck, worst_card)


sym = ['♥', '♦', '♠', '♣']
nums = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
my_deck = []
played = []

for x in range(2,13):
    generate(x)

generate_ntic()


#all_deck = itertools.product(nums, 2*sym)
all_deck = itertools.product(nums, sym)
deck = list(map(lambda x: x[0]+""+x[1], list(all_deck)))
my_deck = rd.sample(deck, 12)
for x in my_deck:
    deck.remove(x)

played = []
game_input = ""
my_deck = sorted(my_deck, key=my_sort)
print(my_deck)
while(game_input != "end" and len(played) < 104):
	game_input = input("> ")

	while(game_input != "throw"):
		parse_input(game_input)
		game_input = input("> ")

	smp = rd.sample(list(deck), 1)[0]
	deck.remove(smp)
	my_deck.append(smp)
	t = turn(my_deck)
	my_deck = t[0]
	played.append(t[1])
	print(f"throw: {t[1]}")



print(my_deck)
print(played)
print(f"deck sum: {deck_sum}")
