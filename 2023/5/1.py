import regex as re
from bisect import bisect_right
def ranger(ranges): 
    ranges.sort(key=lambda x: x[1])
    def mapper(num):
        ind = bisect_right(ranges, num, key=lambda x: x[1])
        print(ind, len(ranges))
        current = ranges[ind - 1]
        if current[1] <= num < current[2] + current[1]:
            print(current, num)
            return num - current[1] + current[0]
        return num
    return mapper

with open("input") as f:
    x = f.readlines()

vals = []
ranges = []
first = True
for i, line in enumerate(x):
    line.removesuffix("\n")
    if i == 0:
        vals = [int(i) for i in re.findall("[0-9]+", line)]
        continue
    if len(line) == 1:
        continue
    if "map" not in line:
        ranges.append([int(i) for i in re.findall("[0-9]+", line)])
    else:
        if first:
            first = False
            continue
        mapper = ranger(ranges)
        vals = [mapper(value) for value in vals]
        print(vals)
        ranges = []


mapper = ranger(ranges)
vals = [mapper(value) for value in vals]
print(min(vals))
