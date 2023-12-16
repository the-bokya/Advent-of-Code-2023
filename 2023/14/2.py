lines = []
answer = 0
while True:
    try:
        line = input()
    except:
        break
    lines.append(line)

cache_line = dict()
cache_count = dict()
def northwards(lines):
    rank = len(lines)
    tops = [-1 for i in range(len(lines[0]))]

    tilted = [["." for i in range(len(lines[0]))] for j in range(len(lines))]

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            top = tops[x]
            if char == "O":
                tops[x] += 1
                tilted[top+1][x] = "O"
            if char == "#":
                tops[x] = y
                tilted[y][x] = "#"
    tilted = ["".join(i) for i in tilted]
    return tilted

def westwards(lines):
    left = [-1 for i in range(len(lines))]
    tilted = [["." for i in range(len(lines[0]))] for j in range(len(lines))]
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "#":
                left[y] = x
                tilted[y][x] = "#"
            if char == "O":
                left[y] += 1
                tilted[y][left[y]] = "O"
    tilted = ["".join(i) for i in tilted]
    return tilted

#h = hash(":".join(northwards(lines)))
def rotate(lines):
    out = [""]

def cycle(lines):
    l = lines.copy()
    l = northwards(l)
    l = westwards(l)
    l.reverse()
    l = [i[::-1] for i in l]
    l = northwards(l)
    l = westwards(l)
    l.reverse()
    l = [i[::-1] for i in l]
    return l

i = 0
l = lines.copy()

while True:
   l = cycle(l) 
   h = hash(":".join(l))
   if h in cache_line:
       cycle_start = cache_count[h]
       hash_repeated = h
       break
   i += 1
   cache_count[h] = i
   cache_line[h] = l

repeated = (1000000000 - cycle_start) % (i + 1 - cycle_start) + cycle_start
count = 0
rank = len(lines)
cache_count_inverted = {x:y for y, x in cache_count.items()}
repeated_line = cache_line[cache_count_inverted[repeated]]
for i in repeated_line:
    rounded = i.count("O")
    count += rounded * rank
    rank -= 1
print(count)
