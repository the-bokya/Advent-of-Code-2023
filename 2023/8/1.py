import regex as re
instructions = []
locs = dict()
with open("input") as f:
    it = -1
    for i in f:
        i = i.removesuffix("\n")
        it += 1
        if it == 0:
            instructions = i
            continue
        if it == 1:
            continue
        loc, left, right = re.findall("[A-Z][A-Z][A-Z]", i)
        locs[loc] = dict()
        locs[loc]["L"] = left
        locs[loc]["R"] = right
        if it == 2:
            current = loc

steps = 0
total_instructions = len(instructions)
while True:
    step = instructions[steps % total_instructions]
    current = locs[current][step]
    print(step, current)
    steps += 1
    if current == "ZZZ":
        print(steps)
        break
