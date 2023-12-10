from collections import Counter
cards = []
with open("sample_2") as f:
    for i in f:
        i = i.removesuffix("\n")
        a, b = i.split(" ")
        b = int(b)
        cards.append([a, b])
strengths = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
def type(a):
    c = Counter(a)
    occurences = sorted(c.values(), reverse=True)
    if occurences[0] == 5:
        return 1
    if occurences[0] == 4:
        return 2
    if occurences[0] == 3:
        if occurences[1] == 2:
            return 3
        return 4
    if occurences[0] == 2:
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
