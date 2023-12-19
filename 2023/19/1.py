import regex as re
lines = []
def funcify(s):
    if ":" in s:
        cond, redir = s.split(":") 
        part = cond[0]
        op = cond[1]
        num = int(cond[2:])
        if op == "<":
            return lambda x: redir if x[part] < num else "N"
        if op == ">":
            return lambda x: redir if x[part] > num else "N"
    return lambda x: s

workflows = dict()
workstage = True
parts = []
while True:
    try:
        current = input()
        if current == "":
            workstage = False
            continue
        
        if workstage:
            wid = re.search("[a-z]*", current)[0]
            funcs = re.findall("{(.*)}", current)[0]
            funcs = funcs.split(",")
            funcs = [funcify(func) for func in funcs]
            workflows[wid] = funcs
        else:
            partsline = re.findall("{(.*)}", current)[0]
            partsline = partsline.split(",")
            part = dict()
            for i in partsline:
                a, b = i.split("=")
                part[a] = int(b)
            parts.append(part)
            

    except Exception as e:
        break

def search(i, wid):
    funcs = workflows[wid]
    for func in funcs:
        res = func(i)
        if res in "AR":
            return res
        if res == "N":
            continue
        return search(i, res)
count = 0
for i in parts:
    if search(i, "in") == "A":
        count += sum(i.values())
print(count)

