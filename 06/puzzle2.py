from rich import print

data = []

with open("input", "r") as f:
    data = f.read()

l = len(data)
s = 0
b = data[s : s + 14]

while len(b) != len(set(b)):
    if l >= 14:
        b = data[s : s + 14]
        s += 1
        l -= 1

print(b)
print(s + 13)
