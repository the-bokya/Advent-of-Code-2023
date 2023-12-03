import regex as re

nums = []
grid = []
with open("input") as f:
    i = 0
    for row in f:
        current = re.findall("\d+|[!-)]|.", row)
        j = 0
        grid_row = []
        for part in current:
            grid_row.extend([part]*len(part))
            if part.isnumeric():
                nums.append([i, j, part])
            j += len(part)
        grid.append(grid_row)
        i += 1
"""
print(nums)
print(grid, len(grid), len(grid[0]))
"""
def finder(i, j, num):
    for x in range(max(i - 1, 0), min(len(grid), i+2)):
        for y in range(max(0, j - 1), min(len(grid[0]), j + len(num) + 1)):
                #print(x, y, grid[x][y])
                if not re.match("[\d\.]", grid[x][y]):
                    print(grid[x][y])
                    return True
    return False
count = 0
for num in nums:
    count += int(num[2]) if finder(*num) else 0
print(count)
