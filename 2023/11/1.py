from collections import Counter
nums = []
grid = []

with open("input") as f:
    for i in f:
        i = i.removesuffix("\n")
        grid.append(list(i))

print(grid)
h = set([i for i in range(len(grid))])
v = set([i for i in range(len(grid[0]))])

for i, y in enumerate(grid):
    for j, x in enumerate(y):
        if x == "#":
            try:
                h.remove(i)
            except:
                pass
            try:
                v.remove(j)
            except:
                pass

h = Counter(h)
v = Counter(v)
add_h = 0
for i, y in enumerate(grid):
    add_v = 0
    if h[i]:
        add_h += 1
    for j, x in enumerate(y):
        if v[j]:
            add_v += 1
        if x == "#":
            nums.append([i + add_h, j + add_v])
count = 0
for i, a in enumerate(nums):
    for j, b in enumerate(nums[i+1:]):
        count += abs(a[0] - b[0]) + abs(a[1] - b[1])
print(count)
