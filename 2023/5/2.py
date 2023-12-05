import regex as re
from bisect import bisect_right
def ranger(ranges):
    ranges.sort(key=lambda x: x[1])
    def mapper(pair):
        num = pair[0]
        diff = pair[1]
        news = []
        
        while True:
            ind = bisect_right(ranges, num, key=lambda x: x[1])
            current = ranges[ind - 1]
            # if floor is in range
            if current[1] <= num < current[2] + current[1]:
                # if ceil is in range - check
                if num + diff < current[1] + current[2]:
                    print("a", num, diff, current)
                    news.append([num - current[1] + current[0], diff])
                    return news
                #if ceil not in range - check
                else:
                    news.append([num - current[1] + current[0], current[1] + current[2] - num])
                    diff = num + diff - current[1] - current[2]
                    num = current[1] + current[2]
                    print("b", num, diff, current)
            else:
                #if ceil not in range

                #if next range available
                if len(ranges) > ind:
                    #if not in any range - check!
                    if (num + diff - 1) < ranges[ind][1]:
                        news.append([num, diff])
                        print("c", num, diff, current)
                        return news
                    # if ceil in some range
                    else:
                        news.append([num, ranges[ind][1] - num])
                        num = ranges[ind][1]
                        diff -= ranges[ind][1] - num
                        print("d", num, diff, current)
                else:
                    print("e")
                    news.append([num, diff])
                    return news
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
        vals = [[int(j) for j in i.split(" ")] for i in re.findall("[0-9]+ [0-9]+", line)]
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
        new_vals = []
        for pair in vals:
            new_vals.extend(mapper(pair))
        vals = new_vals
        print(vals)
        ranges = []


mapper = ranger(ranges)
new_vals = []
for pair in vals:
    new_vals.extend(mapper(pair))
vals = new_vals
vals = list(filter(lambda x: x[1] > 0, vals))
print(min(vals)[0])
