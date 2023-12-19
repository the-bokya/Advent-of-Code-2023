import regex as re
import itertools
lines = []

workflows = dict()
parts = []
while True:
    try:
        current = input()
        wid = re.search("[a-z]*", current)[0]
        funcs = re.findall("{(.*)}", current)[0]
        funcs = funcs.split(",")
        workflows[wid] = funcs

    except Exception as e:
        break
part = {x: {i for i in range(1, 4001)} for x in "xmas"}

def search(part, wid="in"):
    accepted = []
    for work in workflows[wid]:
        if ":" in work:
            cond, dest = work.split(":")
            statement = re.findall("([x|m|a|s])([<|>])(\d*)", cond)[0]
            if len(statement):
                alphabet, op, num = statement
                num = int(num)
                first_part = part.copy()
                second_part = part.copy()
                given = part[alphabet]
                if op == "<":
                    first_part[alphabet] = given.difference({i for i in range(num, 4001)})
                    second_part[alphabet] = given.difference({i for i in range(1, num)})
                if op == ">":
                    first_part[alphabet] = given.difference({i for i in range(1, num + 1)})
                    second_part[alphabet] = given.difference({i for i in range(num + 1, 4001)})
                
                part = second_part
                if dest == "A":
                    accepted.append([first_part, wid])
                    continue
                if dest != "R":
                    accepted.extend(search(first_part, dest))
                    continue
        else:
            if work == "A": 
                accepted.append([part, wid])
                continue
            if work != "R":
                accepted.extend(search(part, work))
                continue
    return accepted

count = 0
for x in search(part):
    count_c = 1
    for j in x[0]:
        count_c *= (len(x[0][j[0]]))
    count += count_c
print(count)

