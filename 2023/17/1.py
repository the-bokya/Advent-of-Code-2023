import heapq
lines = []

while True:
    try:
        line = input()
        line = [int(i) for i in list(line)]
    except:
        break
    lines.append(line)

def neighbours(i, j):
    neighbours = []
    try:
        neighbours.append([grid[i][j + 1], "r"])
    except:
        pass
    try:
        neighbours.append([grid[(i - 1) % (height + 1)][j], "u"])
    except:
        pass
    try:
        neighbours.append([grid[i][(j - 1) % (width + 1)], "l"])
    except:
        pass
    try:
        neighbours.append([grid[i + 1][j], "d"])
    except:
        pass
    return neighbours

class cell:
    def __init__(self, i, j, val):
        self.i = i
        self.j = j
        self.val = val
        self.paths = dict()


height = len(lines)
width = len(lines[0])
grid = [[cell(i, j, lines[i][j]) for j in range(width)] for i in range(height)]

visited = []
first = grid[0][0]
first.paths["d"] = {0: 0}
queue = [[0, "d", 0, 0, 0]]

opposites = {"d": "u", "u": "d", "l": "r", "r": "l"}

while True:
    if len(queue) == 0:
        break
    short, dirxn, steps, current_i, current_j = heapq.heappop(queue)
    current = grid[current_i][current_j]
    nebs = neighbours(current.i, current.j)
    for neb, neb_dirxn in nebs:
        neb_steps = 1
        new_neb_short = short + neb.val
        add_to_queue = False
        if dirxn == opposites[neb_dirxn]:
            continue
        if dirxn == neb_dirxn:
            neb_steps = steps + 1
            if steps == 3:
                continue
        if neb_dirxn not in neb.paths:
            neb.paths[neb_dirxn] = {neb_steps: new_neb_short}
            add_to_queue = True
        else:
            if neb_steps not in neb.paths[neb_dirxn]:
                neb.paths[neb_dirxn][neb_steps] = new_neb_short
                add_to_queue = True
            elif neb.paths[neb_dirxn][neb_steps] > new_neb_short:
                neb.paths[neb_dirxn][neb_steps] = new_neb_short
                add_to_queue = True
        if add_to_queue:
            heapq.heappush(queue, [new_neb_short, neb_dirxn, neb_steps, neb.i, neb.j])

height = len(grid)
width = len(grid[0])
last = grid[-1][-1]
least = min([min(i.values()) for i in last.paths.values()])
print(least)
