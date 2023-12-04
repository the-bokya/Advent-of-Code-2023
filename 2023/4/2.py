from collections import Counter
import regex as re

cards = Counter()
def scorer(x):
    card, x = x.split(": ")
    card_num = int(re.search("\d+", card)[0])
    cards[card_num] += 1
    print(card_num)
    a, b = x.split(" | ")
    a = re.findall("\d+", a)
    b = re.findall("\d+", b)
    a = [int(i) for i in a]
    b = [int(i) for i in b]
    print(b)
    store = Counter(a)
    count = 0
    matches = []
    for i in b:
        if store[i]:
            count += 1
    for i in range(cards[card_num]):
        for j in range(card_num + 1, card_num + count + 1):
            cards[j] += 1
    return count
count = 0
with open("input") as f:
    for i in f:
        i = i.removesuffix("\n")
        prev = scorer(i)
print(sum(cards.values()))
