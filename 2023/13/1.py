inps = []
lines = []
def solve(lines, cache, height, hor=True):
    print(lines)
    if lines == lines[::-1] and len(lines) % 2 == 0:
        return height // 2 + 1
    first = lines[0]
    last = lines[-1]
    print(cache, first, last)
    fst = True
    for elem in [first, last]:
        indices = cache[elem].copy()
        rev = False
        if fst:
            mand = 0
        else:
            mand = height - 1
            rev = True
        print(height, mand, elem, indices, fst)
        fst = False
        indices.remove(mand)
        for i, a in enumerate(indices):
            if rev:
                current = lines[a: mand + 1]
            else:
                current = lines[mand: a + 1]
            if current == current[::-1] and (a + mand) % 2 == 1:
                if hor:
                    return ((a + mand + 1) // 2) * 100
                return (a + mand + 1) // 2
    return 0

answer = 0
def cachify(inp):
    lines = []
    cache = dict()
    i = 0
    for line in inp:
        line = line.replace("#", "1")
        line = line.replace(".", "0")
        line = int(line, base=2)
        if line not in cache:
            cache[line] = []
        cache[line].append(i)
        lines.append(line)
        i += 1
    return lines, cache

while True:
    try:
        line = input()
    except:
        break
    if line == "":
        inps.append(lines)
        lines = []
    else:
        lines.append(line)

inps.append(lines)

for inp in inps:
    hor_size = len(inp)
    ver_size = len(inp[0])
    rot_lines = [["" for i in range(hor_size)] for j in range(ver_size)]
    for i, y in enumerate(inp):
        for j, x in enumerate(y):
            rot_lines[j][i] = x
    rot_lines = ["".join(i) for i in rot_lines]
    hor = cachify(inp)
    x = solve(hor[0], hor[1], hor_size)
    ver = cachify(rot_lines)
    y = solve(ver[0], ver[1], ver_size, hor=False)
    print("ans", x, y)
    answer += x + y

print(answer)
