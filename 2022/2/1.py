def scorer(a, b):
    op = ["A", "B", "C"]
    us = ["X", "Y", "Z"]
    score = us.index(b) + 1
    outcome = (us.index(b) - op.index(a)) % 3
    if outcome == 0:
        score += 3
    elif outcome == 1:
        score += 6
    return score

with open("input") as f:
    count = 0
    for i in f:
        i = i.removesuffix("\n")
        a, b = i.split(" ")
        count += scorer(a, b)

    print(count)
