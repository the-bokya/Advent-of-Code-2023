numses = []
with open("input") as f:
    for i in f:
        i = i.removesuffix("\n")
        numses.append([int(j) for j in i.split(" ")])

print(numses)

def oasis(nums):
    if all(map(lambda x: x == 0, nums)):
        return 0
    diffs = []
    prev = nums[0]
    for i in nums[1:]:
        diffs.append(i - prev)
        prev = i
    
    return oasis(diffs) + nums[-1]

print(sum(list(map(oasis, numses))))
