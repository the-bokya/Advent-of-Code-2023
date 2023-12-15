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
def stringify(gears):
    return ",".join([str(i) for i in gears])
@cache
def ways(line, gears, touched = False):
    if len(gears) == 0:
        if "#" not in line:
            return 1
        return 0
    gears = [int(i) for i in gears.split(",")]
    if len(line) == 0:
        if len(gears) == 0:
            return 1
        if len(gears) == 1 and gears[0] == 0:
            return 1
        return 0

    current = line[0]
    gear = gears[0]
    match current:
        case "#":
            if gear == 0:
                return 0
            return ways(line[1:], stringify([gear - 1] + gears[1:]), True)
        case "?":
            if gear == 0:
                return ways(line[1:], stringify(gears[1:]), False)
            if not touched:
                return ways(line[1:], stringify(gears), False) + ways(line[1:], stringify([gear - 1] + gears[1:]), True)
            return ways(line[1:], stringify([gear - 1] + gears[1:]), True)
        case ".":
            if touched and gear > 0:
                return 0
            if gear == 0:
                return ways(line[1:], stringify(gears[1:]))
            return ways(line[1:], stringify(gears))
total = 0
for i in lines:
    line = re.match("[#|.|?]+", i)[0]
    reduced = []
    gears = re.findall("[0-9]+", i)
    gears *= 5
    gears = ",".join(gears)
    line = ((line + "?") * 5)[:-1]
    count = ways(line, gears)
    total += count
print(total)
