import regex as re
from math import lcm
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
        loc, left, right = re.findall("[0-9|A-Z]{3}", i)
        locs[loc] = dict()
        locs[loc]["L"] = left
        locs[loc]["R"] = right
        if it == 2:
            current = loc

total_instructions = len(instructions)
currents = list(filter(lambda x: x.endswith("A"), locs.keys()))
total_paths = len(currents)
print(currents)

current = currents[1]
till_Z = []
for current in currents:
    steps = 0
    while True:
       current = locs[current][instructions[steps % total_instructions]]
       steps += 1
       if current.endswith("Z"):
           print(steps, current)
           till_Z.append(steps)
           break
print(lcm(*till_Z))
