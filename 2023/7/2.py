from collections import Counter
cards = []
with open("input") as f:
    for i in f:
        i = i.removesuffix("\n")
        a, b = i.split(" ")
        b = int(b)
        cards.append([a, b])
strengths = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
def type(a):
    new = a.replace("J", "")
    c = Counter(new)
    occurences = sorted(c.values(), reverse=True)
    js = a.count("J")
    if js == 5:
        return 1
    largest = occurences[0] + js
    if largest == 5:
        return 1
    if largest == 4:
        return 2
    if largest == 3:
        if occurences[1] == 2:
            return 3
        return 4
    if largest == 2:
        if occurences[1] == 2:
            return 5
        return 6
    return 7
    
def strength(card):
    out = []
    for i in list(card):
        out.append(strengths.index(i))
    print(out)
    return out

def rank(cards):
    cards = sorted(cards, key=lambda card: [type(card[0]), strength(card[0])], reverse=True)
    out = 0
    for i, card in enumerate(cards):
        out += (i+1) * card[1]
    return out

print(rank(cards))
