lines = []
while True:
    try:
        line = input().split(" ")
        line = [line[0], int(line[1]), line[2]]
        lines.append(line)
    except:
        break

print(lines)
height = 10

x = 0
total = 0
outer = 0
for i in lines:
    outer += i[1]
    match i[0]:
        case "D":
            x += i[1]
        case "U":
            x -= i[1]
            total -= i[1]
        case "L":
            total -= (i[1]) * (height - x)
        case "R":
            total += (i[1]) * (height - x - 1)
    print(total)

print(total + outer + 1)
