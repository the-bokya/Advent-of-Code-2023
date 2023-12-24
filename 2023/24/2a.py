import regex as re
from sympy import Eq, symbols, solve
def lin_eq(a1, b1, c1, a2, b2, c2):
    try:
        return (c2*b1 - c1*b2) / (a1*b2 - a2*b1), (c1*a2 - c2*a1) / (a1*b2 - a2*b1)
    except Exception as e:
        print(e)
        return
in_bound = lambda x: 200000000000000 <= x <= 400000000000000
#in_bound = lambda x: 7 <= x <= 27
def t_to_x(x1, y1, vx1, vy1, x2, y2, vx2, vy2):
    try:
        a, b = lin_eq(vx1, -vx2, x1 - x2, vy1, -vy2, y1 - y2)
    except:
        return -1
    if a > 0 and b > 0:
        x = x1 + vx1*a
        y = y2 + vy2*b
        if in_bound(x) and in_bound(y):
            return (x, y)
    return -1

lines = []

while True:
    try:
        line = [int(i) for i in re.findall("-{0,1}[0-9][0-9]*", input())]
    except:
        break
    lines.append(line)
count = 0
eqs = []
x0, y0, z0 = symbols("x0 y0 z0", integer=True)
vx0, vy0, vz0 = symbols("vx0 vy0 vz0", integer=True)
for i, line in enumerate(lines[:3]):
    t = symbols(f" t{i} ")
    x, y, z, vx, vy, vz = line[:6]
    eqs.append(Eq(x0 + vx0*t, x + vx*t))
    eqs.append(Eq(y0 + vy0*t, y + vy*t))
    eqs.append(Eq(z0 + vz0*t, z + vz*t))
solution = solve(eqs)
print(solution)
