from functools import reduce
def comp(x):

    bs = x.split("; ")
    colors = {"red": 0, "green": 0, "blue": 0}
    for j in bs:
        c = j.split(", ")
        for i in c:
            num, color = i.split(" ")
            num = int(num)
            colors[color] = max(colors[color], num)
    return colors

    return True
with open("input") as f:
    count = 0
    for i in f:
        i = i.removesuffix("\n")
        a, b = i.split(": ")
        g_id = int(a.removeprefix("Game "))
        power = reduce(lambda x, y: x*y, comp(b).values())
        count += power
print(count)
