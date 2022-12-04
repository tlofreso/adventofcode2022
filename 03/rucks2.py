from rich import print

with open("input", "r") as f:
    data = f.read().splitlines()

def get_group(lst):
    for i in range(0, len(lst), 3):
        yield lst[i:i + 3]

items = []
groups = get_group(data)
for group in groups:
    k, = set(group[0]) & set(group[1]) & set(group[2])
    items.append(k)

totals = []

for item in items:
    if item.isupper():
        totals.append(ord(item) - 38)
    if item.islower():
        totals.append(ord(item) - 96)

print(sum(totals))