grid = []
with open("input") as f:
    for i in f:
        i = i.removesuffix("\n")
        grid.append(list(i))


for i, y in enumerate(grid):
    for j, x in enumerate(y):
        if x == "S":
            s = [i, j]
            break


def neighbours(point):
    up = False
    down = False
    left = False
    right = False
    match char(point):
        case "S":
            left, right, up, down = [True for i in range(4)]
        case "F":
            down, right = True, True
        case "L":
            up, right = True, True
        case "7":
            down, left = True, True
        case "|":
            down, up = True, True
        case "-":
            left, right = True, True
        case "J":
            left, up = True, True
    
    out = []
    if left:
        try:
            c = move(point, 0, -1)
            if char(c) in list("LF-S"):
                out.append(c)
        except Exception as e:
            print(e)
    if right:
        try:
            c = move(point, 0, 1)
            if char(c) in list("J-7S"):
                out.append(c)
        except Exception as e:
            print(e)
    if up:
        try:
            c = move(point, -1, 0)
            if char(c) in list("|F7S"):
                out.append(c)
        except Exception as e:
            print(e)
    if down:
        try:
            c = move(point, 1, 0)
            if char(c) in list("|JLS"):
                out.append(c)
        except Exception as e:
            print(e)

    return out
def char(point):
    return grid[point[0]][point[1]]
height = len(grid)
width = len(grid[0])

def move(point, i, j):
    # just to catch indexError
    grid[(point[0] + i) % (height + 1)][(point[1] + j) % (width + 1)]
    return [point[0] + i, point[1] + j]

loop_max = []
steps_max = 0
shejari = neighbours(s)
print(shejari)
for i in shejari:
    current = i
    steps = 1
    loop = [s]
    prev = s
    while True:
        if char(current) == "S":
            if steps > steps_max:
                steps_max = steps
                loop_max = loop
            break
        shejari = neighbours(current)
        try:
            if prev in shejari:
                shejari.remove(prev)
            prev = current
            loop.append(current)
            current = shejari[0]
        except:
            break
        steps += 1

print((steps_max + 1)//2)
