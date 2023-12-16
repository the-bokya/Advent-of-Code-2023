def hash_char(val, char):
    asc = ord(char)
    val += asc
    val *= 17
    val %= 256
    return val

def hash_word(word):
    val = 0
    for char in word:
        val = hash_char(val, char)
    return val

class box:

    def __init__(self, box_num):
        self.box_num = box_num
        self.label_to_focal = dict()
        self.lenses = []
    def insert(self, label, focal_length):
        self.label_to_focal[label] = int(focal_length)
        if label not in self.lenses:
            self.lenses.append(label)
    def remove(self, label):
        self.lenses.remove(label)
    def power(self):
        out = 0
        for rank, label in enumerate(self.lenses):
            out += (self.box_num + 1) * (rank + 1) * (self.label_to_focal[label])
        return out

line = input()
boxes = [box(i) for i in range(256)]

for i in line.split(","):
    if "=" in i:
        label, focal_length = i.split("=")
        h = hash_word(label)
        current_box = boxes[h]
        current_box.insert(label, focal_length)
    else:
        label = i[:-1]
        h = hash_word(label)
        current_box = boxes[h]
        try:
            current_box.remove(label)
        except:
            pass

print(sum(box.power() for box in boxes))
