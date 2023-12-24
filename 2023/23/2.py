import threading
grid = []

def neighbours(i, j):
    neighbours = []
    try:
        neighbours.append([i, j + 1, grid[i][j + 1], ">"])
    except:
        pass
    try:
        neighbours.append([i - 1, j, grid[(i - 1) % (height + 1)][j], "^"])
    except Exception as e:
        pass
    try:
        neighbours.append([i, j - 1, grid[i][(j - 1) % (width + 1)], "<"])
    except:
        pass
    try:
        neighbours.append([i+1, j, grid[i + 1][j], "v"])
    except:
        pass
    return neighbours

while True:
    try:
        grid_line = list(input())
    except:
        break
    grid.append(grid_line)


height = len(grid)
width = len(grid[0])

start = (0, grid[0].index("."))
end = (height - 1, grid[-1].index("."))
p = []
opps = {">": "<", "<": ">", "^": "v", "v": "^"}
embarked_upon = set([start])

queue = [(start, "v", start)]
conns = dict()
while len(queue):
    (i, j), dirxn, (si, sj) = queue.pop(0)
    embarked_upon.add((i, j))
    steps = 1
    if (start == (i, j)):
        steps = 0
    di, dj, ddirxn = i, j, dirxn
    while True:
        nebs = list(filter(lambda neb: (neb[0], neb[1]) not in embarked_upon and opps[neb[3]] != ddirxn and neb[2] != "#", neighbours(di, dj)))
        if len(nebs) > 1:
            if (si, sj) not in conns:
                conns[(si, sj)] = set()
            conns[(si, sj)].add(((di, dj), steps))
            if (di, dj) not in conns:
                conns[(di, dj)] = set()
            conns[(di, dj)].add(((si, sj), steps))
            nx = [((ni, nj), ndirxn, (di, dj)) for ni, nj, nchar, ndirxn in nebs]
            queue.extend(nx)
            break
        elif len(nebs) == 1:
            di, dj, _, ddirxn = nebs[0]
            if (di, dj) == end:
                if (si, sj) not in conns:
                    conns[(si, sj)] = set()
                conns[(si, sj)].add(((di, dj), steps + 1))
                if (di, dj) not in conns:
                    conns[(di, dj)] = set()
                conns[(di, dj)].add(((si, sj), steps))
                break 
        else:
            break
        steps += 1

"""
for x in conns:
    i, j = x
    grid[i][j] = "O"

for i in grid:
    print("".join(i))
"""
biggest = 0
print(conns)
def search(current=start, prev=set(), steps=0):
    if current == end:
        return steps
    if current in prev:
        return 0
    prev.add(current)
    big = 0
    threads = []
    for nxt, nxt_step in conns[current]:
        big = max(big, search(nxt, prev.copy(), steps + nxt_step))
    return big

print(search())
