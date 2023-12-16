lines = []
answer = 0
while True:
    try:
        line = input()
    except:
        break
    lines.append(line)


rank = len(lines)
tops = [-1 for i in range(len(lines[0]))]

tilted = [["." for i in range(len(lines[0]))] for j in range(len(lines))]

for y, line in enumerate(lines):
    print(tops)
    for x, char in enumerate(line):
        top = tops[x]
        if char == "O":
            tops[x] += 1
            tilted[top+1][x] = "O"
        if char == "#":
            tops[x] = y
            tilted[y][x] = "#"

count = 0
for i in tilted:
    rounded = i.count("O")
    count += rounded * rank
    print("".join(i))
    rank -= 1
print(count)

