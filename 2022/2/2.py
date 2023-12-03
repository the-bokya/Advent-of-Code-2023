def scorer(a, b):
    op = ["A", "B", "C"]
    us = ["X", "Y", "Z"]
    usind = us.index(b)
    opind = op.index(a)
    score = usind * 3 + 1

    if usind == 1:
        score += opind
    elif usind == 0:
        score += (opind - 1) % 3
    elif usind == 2:
        score += (opind + 1) % 3
    return score
    
print(scorer("A", "Y"))
print(scorer("B", "X"))
print(scorer("C", "Z"))
with open("input") as f:
    count = 0
    for i in f:
        i = i.removesuffix("\n")
        a, b = i.split(" ")
        count += scorer(a, b)

    print(count)
