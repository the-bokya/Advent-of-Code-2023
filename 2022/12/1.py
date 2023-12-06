cache = dict()
with open("input") as f:
    grid = [list(i) for i in f.read().split("\n")]
grid = grid[:len(grid) - 1]


found = 0
for i, x in enumerate(grid):
    for j, y in enumerate(x):
        if y == "S":
            start = [i, j]
            found += 1
            continue
        if y == "E":
            end = [i, j]
            found += 1
            continue
        if found == 2:
            break
            found += 1
            continue
width = len(grid[0])
height = len(grid)
smallest = width * height
def already(i, j, steps):
    if i in cache:
        if j in cache[i]:
            if cache[i][j] >= steps:
                cache[i][j] = steps
                return False
            return True
        cache[i][j] = steps
        return False
    cache[i] = dict()
    return False
def compare(src, i, j):
    if i >= height or i < 0 or j >= width or j < 0:
        return False
    dest = grid[i][j]
    if src == "S":
        return True
    return ord(src) + 1 >= ord(dest)

def search(i, j, steps):
    char = grid[i][j]
    global smallest
    if [i, j] == end:
        smallest = min(steps, smallest)
        return 0
    if 0 < j:
        if not already(i, -j, steps) and compare(char, i, j - 1):
            search(i, j - 1, steps + 1)
    if width - 1 > j:
        if not already(i, -j, steps) and compare(char, i, j + 1):
            search(i, j + 1, steps + 1)
    if 0 < i:
        if not already(i, -j, steps) and compare(char, i - 1, j):
            search(i - 1, j, steps + 1)
    if height > i:
        if not already(i, -j, steps) and compare(char, i + 1, j):
            search(i + 1, j, steps + 1)
search(start[0], start[1], 0)
print(grid, start, end, smallest)
