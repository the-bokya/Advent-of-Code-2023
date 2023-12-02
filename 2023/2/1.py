colors = {"red": 12, "green": 13, "blue": 14}
def comp(x):

    bs = x.split("; ")
    for j in bs:
        c = j.split(", ")
        for i in c:
            num, color = i.split(" ")
            num = int(num)
            if num > colors[color]:
                return False

    return True
with open("input") as f:
    count = 0
    for i in f:
        i = i.removesuffix("\n")
        a, b = i.split(": ")
        g_id = int(a.removeprefix("Game "))
        if comp(b):
            count += g_id
print(count)
