import regex as re
import math
with open("input") as f:
    tiempo, dist = f.readlines()

def ways(time, dist):
    most = (time + math.sqrt(time**2 - 4*dist))/2
    if most == int(most):
        most -= 1
    most = int(most)
    least = time - most
    print(time, dist, least, most, "meow")
    return time - 2 * least + 1

pattern = re.compile("[0-9]+")
tiempo = re.findall(pattern, tiempo)
dist = re.findall(pattern, dist)
tiempo = [int(i) for i in tiempo]
dist = [int(i) for i in dist]

answer = 1
for i in range(len(tiempo)):
    answer *= ways(tiempo[i], dist[i])
print(answer)
