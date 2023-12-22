from collections import deque
lines = []
while True:
    try:
        line = list(input())
    except:
        break
    lines.append(line)

height = len(lines)
width = len(lines[0])
for i, y in enumerate(lines):
    for j, x in enumerate(y):
        if x == "S":
            starting = [i, j]
given = 64
visited = {(starting[0], starting[1])}
queue = deque([[*starting, 0]])
count = 0
while len(queue):
    i, j, steps = queue.popleft()
    if steps > given:
        continue
    if steps % 2 == 0:
        count += 1
    neighbours = []
    if i > 0:
        neighbours.append([i - 1, j])
    if j > 0:
        neighbours.append([i, j - 1])
    if i < height - 1:
        neighbours.append([i + 1, j])
    if j < width - 1:
        neighbours.append([i, j + 1])
    for neb in neighbours:
        if lines[neb[0]][neb[1]] == "#":
            continue
        if (neb[0], neb[1]) in visited:
            continue
        visited.add((neb[0], neb[1]))
        queue.append([*neb, steps + 1])

print(count)
