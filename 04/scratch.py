from rich import print

with open("input", "r") as f:
    data = f.read().splitlines()

for line in data:
    a, b, x, y = map(int, line.replace(",", "-").split("-"))
    print(a, b, x, y)
