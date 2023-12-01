import regex as re
count = 0
def to_num(x):
    s = {"one": 1,
         "two": 2,
         "three": 3,
         "four": 4,
         "five": 5,
         "six": 6,
         "seven": 7,
         "eight": 8,
         "nine": 9,
         "zero": 0,
         }
    if x in s:
        return s[x]
    return int(x)
with open("input") as f:
    for i in f:
        c = re.findall("\d|one|two|three|four|five|six|seven|eight|nine|zero", i, overlapped=True)
        num = to_num(c[0])*10 + to_num(c[-1])
        count += num
        print(count, num)
