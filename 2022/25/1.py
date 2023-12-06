def snafu_normal(snafu):
    normal = 0
    for i in snafu:
        normal *= 5
        if i.isnumeric():
            normal += int(i)
        elif i == "-":
            normal -= 1
        elif i == "=":
            normal -= 2
    print(normal)
    return normal

def normal_snafu(normal):
    base_5 = []
    while normal > 0:
        base_5.append(normal % 5)
        normal //= 5
    snafu = ""
    carry = False
    char_map = {1: "1", 2: "2", 3: "=", 4: "-", 5: "0", 0: "0"}
    for i in base_5:
        if carry:
            i = (int(i) + 1)
            carry = False
        if i > 2:
            carry = True
        snafu = char_map[i] + snafu
    if carry:
        snafu = "1" + snafu
    return snafu
        

with open("input") as f:
    count = 0
    for i in f:
        i = i.removesuffix("\n")
        count += snafu_normal(i)

print(normal_snafu(count))
