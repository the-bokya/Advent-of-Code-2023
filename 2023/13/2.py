inps = []
lines = []
def solve(lines, cache, height, hor=True, stale_x=-1):
    print("s", stale_x)
    if lines == lines[::-1] and len(lines) % 2 == 0:
        return height // 2 + 1
    first = lines[0]
    last = lines[-1]
    fst = True
    for elem in [first, last]:
        indices = cache[elem].copy()
        rev = False
        if fst:
            mand = 0
        else:
            mand = height - 1
            rev = True
        fst = False
        indices.remove(mand)
        for i, a in enumerate(indices):
            if rev:
                current = lines[a: mand + 1]
            else:
                current = lines[mand: a + 1]
            if current == current[::-1] and (a + mand) % 2 == 1:
                if hor:

                    out = ((a + mand + 1) // 2) * 100
                else:
                    out = (a + mand + 1) // 2
                if out != stale_x:
                    return out
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

def off_by_one(lines):
    offs = []
    for i, a in enumerate(lines):
        for j, b in enumerate(lines[i + 1:]):
            xor = a ^ b
            if xor & (xor - 1) == 0:
                offs.append([a, b]) 
    if len(offs):
        print(offs)
    return offs

inps.append(lines)

for inp in inps:
    hor_size = len(inp)
    ver_size = len(inp[0])
    rot_lines = [["" for i in range(hor_size)] for j in range(ver_size)]
    for i, y in enumerate(inp):
        for j, x in enumerate(y):
            rot_lines[j][i] = x
    rot_lines = ["".join(i) for i in rot_lines]
    hor_lines, hor_cache = cachify(inp)
    x, y = 0, 0
    xs, ys = [], []
    stale_x = solve(hor_lines, hor_cache, hor_size)
    for offs in off_by_one(list(hor_cache.keys())):
        current_hor_lines = hor_lines.copy()
        current_hor_cache = hor_cache.copy()
        a, b = offs
        current_hor_lines = [a if i == b else i for i in current_hor_lines]
        current_hor_cache[a].extend(current_hor_cache[b])
        del current_hor_cache[b]
        x = solve(current_hor_lines, current_hor_cache, hor_size, hor=True, stale_x=stale_x)
        if x > 0:
            answer += x
            xs.append(x)

    if x == 0:
        ver_lines, ver_cache = cachify(rot_lines)
        stale_y = solve(ver_lines, ver_cache, ver_size, hor=False)
        for offs in off_by_one(list(ver_cache.keys())):
            current_ver_lines = ver_lines.copy()
            current_ver_cache = ver_cache.copy()
            a, b = offs
            current_ver_lines = [a if i == b else i for i in current_ver_lines]
            current_ver_cache[a].extend(current_ver_cache[b])
            del current_ver_cache[b]
            y = solve(current_ver_lines, current_ver_cache, ver_size, hor=False, stale_x=stale_y)
            if y > 0:
                answer += y
                ys.append(y)
    print(xs, ys, "answers")

print(answer)
