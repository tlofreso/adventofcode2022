from posixpath import split
from rich import print

with open("input", "r") as f:
    data = f.read().splitlines()


def split_strings(line):
    x = len(line)//2
    str1 = line[:x]
    str2 = line[x:]

    for e in str1:
        if e in str2:
            if e.isupper():
                return ord(e) - 38
            return ord(e) - 96

items = []

for line in data:
    items.append(split_strings(line))

t = sum(items)
print(t)


# l_alpha = 'abcdefghijklmnopqrstuvwxyz'
# u_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# 
# for e in l_alpha:
#     print(ord(e))
# 
# for e in u_alpha:
#     print(ord(e))

