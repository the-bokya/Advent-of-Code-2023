from collections import Counter
import regex as re

cards = Counter({1:0, 2:0, 3:0, 4:0, 5:0, 6: 0})
def scorer(x):
    card, x = x.split(": ")
    card_num = int(re.search("\d+", card)[0])
    cards[card_num] += 1
    a, b = x.split(" | ")
    a = re.findall("\d+", a)
    b = re.findall("\d+", b)
    a = [int(i) for i in a]
    b = [int(i) for i in b]
    store = Counter(a)
    count = 0
    for i in b:
        if store[i]:
            count += 1
    print("Going through card", card_num)
    print("Total cards (before):", cards)

    for i in range(cards[card_num]):
        for j in range(card_num + 1, card_num + count + 1):
            cards[j] += 1
    print(f"After {count} matches of {card_num}, of which we have {cards[card_num]} copies, additional cards: {[i for i in range(card_num + 1, card_num + count + 1)]} * {cards[card_num]}")
    print("total cards (after):", cards)
    return count
count = 0
with open("input") as f:
    for i in f:
        i = i.removesuffix("\n")
        prev = scorer(i)
print(sum(cards.values()))
