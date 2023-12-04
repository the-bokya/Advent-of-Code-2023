from collections import Counter
import regex as re
def scorer(x):
    _, x = x.split(": ")
    a, b = x.split(" | ")
    a = re.findall("\d+", a)
    b = re.findall("\d+", b)
    a = [int(i) for i in a]
    b = [int(i) for i in b]
    store = Counter(a)
    count = 0
    for i in b:
        if store[i]:
            if count == 0:
                count = 1
            else:
                count *= 2
    print(a, b)
    return count
count = 0
with open("input") as f:
    for i in f:
        i = i.removesuffix("\n")
        count += scorer(i)

print(count)
        
