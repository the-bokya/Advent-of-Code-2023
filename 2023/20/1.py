lines = []

class ff():
    def __init__(self, module_id, recipients):
        self.recipients = recipients
        self.module_id = module_id
        self.state = False

    def input(self, pulse, iid):
        if pulse == 0:
            self.state = not self.state
            if self.state == False:
                return 0
            return 1

class con():

    def __init__(self, module_id, recipients, inputs):
        self.connections = {i:0 for i in inputs}
        self.recipients = recipients
        self.module_id = module_id

    def input(self, pulse, iid):
        self.connections[iid] = pulse
        if all(self.connections.values()):
            return 0
        return 1

class output():
    def input(self, pulse, iid):
        return

conns = dict()
types = dict()
inputs = dict()
objects = dict()
while True:
    try:
        line = input()
    except:
        break
    lhs, rhs = line.split(" -> ")
    module = lhs
    t = "broadcaster"
    if lhs != "broadcaster":
        t = lhs[:1]
        module = lhs[1:]

    dests = rhs.split(", ")
    for i in dests:
        if i not in inputs:
            inputs[i] = []
        inputs[i].append(module)
    types[module] = t
    conns[module] = dests


objects["output"] = output()
for i, t in types.items():
    if t == "&":
        objects[i] = con(i, conns[i], inputs[i])
    if t == "%":
        objects[i] = ff(i, conns[i])

states = []

lows = 0
highs = 0
low_cache = dict()
high_cache = dict()
for count in range(1000):
    queue = [[i, 0, "broadcaster"] for i in conns["broadcaster"]]
    lows += 1
    while len(queue):
        recipient, pulse, m_id = queue.pop(0)
        if pulse == 1:
            highs += 1
        elif pulse == 0:
            lows += 1
        if recipient not in objects:
            continue
        rec = objects[recipient]
        out_pulse = rec.input(pulse, m_id)
        if out_pulse == None:
            continue
        for out in rec.recipients:
            queue.append([out, out_pulse, recipient])
    state = []
    for i in types:
        if types[i] == "%":
            state.append([i, objects[i].state])
        if types[i] == "&":
            state.append([i, objects[i].connections])
    low_cache[count] = lows
    high_cache[count] = highs
    states.append(state)
print(lows*highs)
