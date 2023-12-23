grid = []
import sys
sys.setrecursionlimit(1000000000)

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

start = [0, grid[0].index(".")]
end = [height - 1, grid[-1].index(".")]
steps_grid = [[-1 for i in range(width)] for j in range(height)]
p = []
def search(i=0, j=start[1], prev=set(), dirxn="v", steps=0, prev_dirxn=""):
    global steps_grid
    global p
    if steps_grid[i][j] < steps:
        steps_grid[i][j] = steps
        if [i, j] == end:
            p = prev
    else:
        return
    for neb in neighbours(i, j):
        neb_i, neb_j, char, neb_dirxn = neb
        if (neb_i, neb_j) in prev:
            continue
        if char == "#":
            continue
        if char in "^><v":
            if char != neb_dirxn:
                continue
        prev_new = prev.copy()
        prev_new.add((neb_i, neb_j))
        search(neb_i, neb_j, prev_new, neb_dirxn, steps + 1)


search()
for x in p:
    i, j = x
    grid[i][j] = "O"

for i in grid:
    print("".join(i))
print(steps_grid[end[0]][end[1]])
