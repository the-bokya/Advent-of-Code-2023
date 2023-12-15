import regex as re
from functools import cache
lines = []
while True:
    try:
        line = input()
    except:
        break
    lines.append(line)
    print(line)

def ways(line, gears, touched = False):
    if len(line) == 0:
        if len(gears) == 0:
            return 1
        if len(gears) == 1 and gears[0] == 0:
            return 1
        return 0
    if len(gears) == 0:
        if "#" not in line:
            return 1
        return 0

    current = line[0]
    gear = gears[0]
    match current:
        case "#":
            if gear == 0:
                return 0
            return ways(line[1:],[gear - 1] + gears[1:], True)
        case "?":
            if gear == 0:
                return ways(line[1:], gears[1:], False)
            if not touched:
                return ways(line[1:], gears, False) + ways(line[1:], [gear - 1] + gears[1:], True)
            return ways(line[1:], [gear - 1] + gears[1:], True)
        case ".":
            if touched and gear > 0:
                return 0
            if gear == 0:
                return ways(line[1:], gears[1:])
            return ways(line[1:], gears)
total = 0
for i in lines:
    line = re.match("[#|.|?]+", i)[0]
    reduced = []
    gears = [int(i) for i in re.findall("[0-9]+", i)]
    count = ways(line, gears)
    total += count
print(total)
