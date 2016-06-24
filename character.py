import string
import random


swag = raw_input("how many random charcters would you like to generate? ")

s = ""
x = int(swag)

for i in range(0, x):
    s += random.choice(string.ascii_letters)

def newline(str):
    lines = []
    for y in xrange(0, len(str), 64):
        lines.append(str[y:y+64])
    return '\n'.join(lines)


a = newline(s)

print '\n'
print a
print '\n'
