import bisect
lines = []
while True:
    try:
        line = [i for i in input()]
        lines.append(line)
    except:
        break

cache = []

height = len(lines)
width = len(line)

hor = dict()
ver = dict()

grid = [[0 for j in range(width)] for i in range(height)]

for i, line in enumerate(lines):
    for j, x in enumerate(line):
        if x != ".":
            if i not in hor:
                hor[i] = []
            hor[i].append([x, j])
            if j not in ver:
                ver[j] = []
            ver[j].append([x, i])

def search(i, j, dirxn):
    print(i, j, dirxn)
    if [i, j, dirxn] in cache:
        return
    cache.append([i, j, dirxn])
    match dirxn:
        case "d":
            if i == height - 1:
                return
            index = bisect.bisect_right(ver[j], i, key=lambda x: x[1])
            try:
                nxt = ver[j][index]
            except:
                for c in range(i, height):
                    grid[c][j] = 1
                return
            for c in range(i, nxt[1] + 1):
                grid[c][j] = 1
        case "u":
            if i == 0:
                return
            index = bisect.bisect_left(ver[j], i, key=lambda x: x[1]) - 1
            if index < 0:
                for c in range(0, i + 1):
                    grid[c][j] = 1
                return
            nxt = ver[j][index]
            for c in range(nxt[1], i + 1):
                grid[c][j] = 1
        case "l":
            if j == 0:
                return
            index = bisect.bisect_left(hor[i], j, key=lambda x: x[1]) - 1
            if index < 0:
                for c in range(0, j + 1):
                    grid[i][c] = 1
                return
            nxt = hor[i][index]
            print(nxt, i, j, "l")
            for c in range(nxt[1], j + 1):
                grid[i][c] = 1
        case "r":
            if j == width - 1:
                return
            index = bisect.bisect_right(hor[i], j, key=lambda x: x[1])
            try:
                nxt = hor[i][index]
            except:
                for c in range(j, width):
                    grid[i][c] = 1
                return
            print(index, i, j, dirxn, hor[i])
            for c in range(j, nxt[1] + 1):
                grid[i][c] = 1
        case _:
            print("meow")
    print(nxt)
    match nxt[0]:
        case "\\":
            if dirxn == "r":
                search(i, nxt[1], "d")
            if dirxn == "l":
                search(i, nxt[1], "u")
            if dirxn == "d":
                search(nxt[1], j, "r")
            if dirxn == "u":
                search(nxt[1], j, "l")
        case "/":
            if dirxn == "r":
                search(i, nxt[1], "u")
            if dirxn == "l":
                search(i, nxt[1], "d")
            if dirxn == "d":
                search(nxt[1], j, "l")
            if dirxn == "u":
                search(nxt[1], j, "r")
        case "-":
            if dirxn in "du":
                search(nxt[1], j, "l")
                search(nxt[1], j, "r")
            else:
                search(i, nxt[1], dirxn)
        case "|":
            if dirxn in "lr":
                search(i, nxt[1], "u")
                search(i, nxt[1], "d")
            else:
                search(nxt[1], j, dirxn)
search(0, 0, "r")
[print("".join([str(i) for i in x])) for x in grid]
print(sum([sum(i) for i in grid]))
