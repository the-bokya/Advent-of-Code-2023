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


line = input()

print(sum([hash_word(word) for word in line.split(",")]))
