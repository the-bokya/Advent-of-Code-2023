bricks = []
b_id = 0
while True:
    try:
        brick = sorted([[int(j) for j in i.split(",")] for i in input().split("~")], key=lambda x: x[::-1])
        brick.append(b_id)
        b_id += 1
    except Exception as e:
        break
    bricks.append(brick)

def intersect(b1, b2):
    if b1[1][0] >= b2[0][0] and b1[0][0]  <= b2[1][0]:
        if b1[1][1] >= b2[0][1] and b1[0][1]  <= b2[1][1]:
            return True
    return False
bricks.sort(key=lambda x: x[1][::-1])
fallen = [bricks[0]]
dependents = dict({i: set() for i in range(b_id)})
depending = dict({i: set() for i in range(b_id)})
for i in range(1, len(bricks)):
    j = len(fallen) - 1
    v_diff = bricks[i][1][2] - bricks[i][0][2]
    while True:
        if j == -1:
            bricks[i][0][2] = 1
            bricks[i][1][2] = bricks[i][0][2] + v_diff
            fallen.append(bricks[i])
            break
        if intersect(fallen[j], bricks[i]):
            if bricks[i][0][2] > fallen[j][1][2]:
                bricks[i][0][2] = fallen[j][1][2] + 1
                bricks[i][1][2] = bricks[i][0][2] + v_diff
                fallen.append(bricks[i])
            break
        j -= 1
    fallen.sort(key=lambda x: x[1][::-1])

for i in range(len(fallen)):
    for j in range(i + 1, len(fallen)):
        a, b = fallen[i], fallen[j]
        if a[1][2] + 1 == b[0][2] and intersect(a, b):
            dependents[a[2]].add(b[2])
            depending[b[2]].add(a[2])
count = 0

for key, values in dependents.items():
    dissed = {key}
    queue = list(values)
    while len(queue):
        current = queue.pop(0)
        if len(depending[current].difference(dissed)) == 0:
            dissed.add(current)
            queue.extend(list(dependents[current]))
    count += len(dissed) - 1



print(count)
