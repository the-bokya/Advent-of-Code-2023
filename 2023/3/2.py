import regex as re
from functools import reduce
grid = []
stars = []
with open("input") as f:
    i = 0
    for row in f:
        current = re.findall("\d+|[!-)]|.", row)
        j = 0
        grid_row = []
        for part in current:
            grid_row.extend([[i, j, part]]*len(part))
            if re.match("\*", part):
                stars.append([i, j, part])
            j += len(part)
        grid.append(grid_row)
        i += 1
"""
print(nums)
print(grid, len(grid), len(grid[0]))
"""
def finder(i, j, num):
    gears = []
    for x in range(max(i - 1, 0), min(len(grid), i+2)):
        for y in range(max(0, j - 1), min(len(grid[0]), j + 2)):
                #print(x, y, grid[x][y])
                if re.match("[\d]", grid[x][y][2]):
                    print(grid[x][y])
                    if grid[x][y] not in gears:
                        gears.append(grid[x][y])
    if len(gears) == 2:
        return reduce(lambda x, y: int(x[2])*int(y[2]), list(gears))
    return 0
count = 0
for star in stars:
    count += finder(*star)
print(count)
