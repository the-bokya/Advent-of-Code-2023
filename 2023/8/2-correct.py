import regex as re
from math import lcm
instructions = []
locs = dict()
with open("sample-correct") as f:
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
till_Zs = []
steps_till_Zs = []
for current in currents:
    steps = 0
    prev = 0
    till_Z = []
    steps_till_Z = []
    while True:
       current = locs[current][instructions[steps % total_instructions]]
       steps += 1
       if current.endswith("Z"):
           print(steps - prev, current)
           reached = [current, steps - prev, steps % total_instructions]
           if reached in till_Z:
               print(steps, reached)
               break
           steps_till_Z.append(steps)
           till_Z.append(reached)
           prev = steps
           continue
    till_Zs.append(till_Z)
    steps_till_Zs.append(steps_till_Z)
    print(till_Zs, steps_till_Zs)

lcms = []
def permutations(steps_till_Zs):
    out = []
    if len(steps_till_Zs) == 0:
        return [[1]]
    for steps in steps_till_Zs[0]:
        for j in permutations(steps_till_Zs[1:]):
            print(j, steps_till_Zs)
            j.append(steps)
            out.append(j)
    return out

perms = permutations(steps_till_Zs)
print(steps_till_Zs)
print(perms)
print(min(map(lambda x: lcm(*x), perms)))
