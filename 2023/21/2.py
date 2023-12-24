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
assert height == width
given = 26501365
max_steps = height * 2 + 1
def p1(max_steps, starting, state=0):
    visited = {(starting[0], starting[1])}
    queue = deque([[*starting, 0]])
    count = 0
    while len(queue):
        i, j, steps = queue.popleft()
        if steps > max_steps:
            continue
        if (steps + state) % 2 == 0:
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
    return count
print(height, width)
diag = given // height - 1
odd_steps = p1(height * 2, (height//2, width//2), 1)
even_steps = p1(height * 2, (height//2, width//2), 0)
odd = ((diag // 2) * 2 + 1) ** 2
even = ((diag + 1) // 2 * 2) ** 2
c_u = p1(height - 1, (height - 1, width // 2), 0)
c_r = p1(height - 1, (height // 2, 0), 0)
c_l = p1(height - 1, (height // 2, width - 1), 0)
c_d = p1(height - 1, (0, width // 2), 0)

s_tl = p1(height // 2 - 1, (height - 1, width - 1), 0)
s_tr = p1(height // 2 - 1, (height - 1, 0), 0)
s_bl = p1(height // 2 - 1, (0, width - 1), 0)
s_br = p1(height // 2 - 1, (0, 0), 0)

l_tl = p1(3 * height // 2 - 1, (height - 1, width - 1), 1)
l_tr = p1(3 * height // 2 - 1, (height - 1, 0), 1)
l_bl = p1(3 * height // 2 - 1, (0, width - 1), 1)
l_br = p1(3 * height // 2 - 1, (0, 0), 1)

total = odd * odd_steps + even * even_steps + c_u + c_d + c_l + c_r + (diag + 1) * (s_br + s_bl + s_tl + s_tr) + (diag) * (l_br + l_bl + l_tl + l_tr)
print(odd , odd_steps , even , even_steps , c_u , c_d , c_l , c_r , (diag + 1) , s_br , s_bl , s_tl , s_tr , diag , l_br , l_bl , l_tl , l_tr)
print(total)
